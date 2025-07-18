# In app.py
import os
import logging
from flask import Flask, request, render_template, send_from_directory
from dotenv import load_dotenv

# Try to import OpenAI, but don't fail if it's not available
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError as e:
    logging.error(f"OpenAI library not available: {e}")
    OPENAI_AVAILABLE = False
    OpenAI = None

# Load environment variables
load_dotenv()

# Configure logging for production
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Security headers
@app.after_request
def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# Health check endpoint for AWS
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'service': 'eduplan-assistant'}, 200

# Serve static files from images folder
@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

# OpenAI client setup - lazy initialization
client = None

def get_openai_client():
    global client
    if client is None:
        if not OPENAI_AVAILABLE:
            logger.error("OpenAI library is not available")
            return None
            
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            logger.error("OPENAI_API_KEY environment variable is not set!")
            return None
        try:
            # Try different initialization methods for compatibility
            import openai
            openai_version = getattr(openai, '__version__', 'unknown')
            logger.info(f"OpenAI library version: {openai_version}")
            
            # Try the newest initialization method first
            try:
                client = OpenAI(api_key=api_key)
                logger.info("OpenAI client initialized with new method")
            except TypeError as e:
                if 'proxies' in str(e):
                    # Older version that doesn't support proxies parameter
                    logger.info("Trying older OpenAI client initialization method")
                    # For older versions, try direct import
                    import openai as openai_module
                    openai_module.api_key = api_key
                    client = openai_module
                    logger.info("OpenAI client initialized with legacy method")
                else:
                    raise e
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {str(e)}")
            logger.error(f"OpenAI version: {getattr(openai, '__version__', 'unknown')}")
            return None
    return client

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Get OpenAI client (lazy initialization)
            openai_client = get_openai_client()
            if openai_client is None:
                logger.error("OpenAI client is not available")
                error_message = "🤖 Oops! My AI buddy needs some setup first. Please check the configuration! 😅"
                return render_template("index.html", response=error_message)

            # Get form data
            subject = request.form.get("subject")
            specialty = request.form.get("specialty")
            grade = request.form.get("grade")
            hoursperday = request.form.get("hoursperday")
            numweeks = request.form.get("numweeks")
            state = request.form.get("state")
            focus = request.form.get("focus")
            format = request.form.get("format")
            user_input = request.form.get("user_input")

            logger.info(f"Generating lesson plan for {subject} - {grade} grade")

            # Check if we have all required environment variables
            required_vars = ["OPENAI_API_KEY", "OPENAI_PROMPT_ID", "OPENAI_PROMPT_VERSION"]
            missing_vars = [var for var in required_vars if not os.environ.get(var)]
            
            if missing_vars:
                logger.error(f"Missing environment variables: {missing_vars}")
                error_message = f"🤖 Oops! I need some configuration first! Missing: {', '.join(missing_vars)}. Please set up your .env file! 😅"
                return render_template("index.html", response=error_message)

            # Send data to OpenAI endpoint - handle different client types
            try:
                if hasattr(openai_client, 'responses'):
                    # New OpenAI client format
                    response = openai_client.responses.create(
                        prompt={
                            "id": os.environ.get("OPENAI_PROMPT_ID"),
                            "version": os.environ.get("OPENAI_PROMPT_VERSION", "5"),
                            "variables": {
                                "subject": subject,
                                "specialty": specialty,
                                "grade": grade,
                                "hoursperday": hoursperday,
                                "numweeks": numweeks,
                                "state": state,
                                "focus": focus
                            }
                        },
                        input=[{"role": "user", "content": user_input}],
                        reasoning={},
                        max_output_tokens=2048,
                        store=True
                    )
                    # Extract plain text from the response
                    plain_text = response.output[0].content[0].text
                else:
                    # Legacy OpenAI client - use completions
                    response = openai_client.completions.create(
                        model="gpt-3.5-turbo-instruct",
                        prompt=f"Create a lesson plan for {subject} ({specialty}) for grade {grade}. Duration: {hoursperday} hours/day for {numweeks} weeks in {state}. Focus: {focus}. Additional details: {user_input}",
                        max_tokens=2048,
                        temperature=0.7
                    )
                    plain_text = response.choices[0].text.strip()
            except AttributeError as e:
                logger.error(f"OpenAI client method not found: {str(e)}")
                raise Exception("OpenAI client configuration error")
            logger.info("Successfully generated lesson plan")

            # Render the response on the page
            return render_template("index.html", response=plain_text)

        except Exception as e:
            logger.error(f"Error generating lesson plan: {str(e)}")
            error_message = "🤖 Oops! My AI buddy is having a little trouble right now. Please try again in a moment! 😅"
            return render_template("index.html", response=error_message)

    return render_template("index.html", response=None)

if __name__ == "__main__":
    # For local development
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

# Export for Vercel (handled in api/index.py)
# Keep this for compatibility
application = app