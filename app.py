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
            # More robust OpenAI client initialization
            import openai
            openai_version = getattr(openai, '__version__', 'unknown')
            logger.info(f"OpenAI library version: {openai_version}")
            
            # Try different initialization methods based on version and available constructors
            client = None
            
            # Method 1: Try legacy approach first (more compatible)
            try:
                # Set API key directly on module (legacy approach)
                openai.api_key = api_key
                client = openai
                logger.info("OpenAI client initialized with legacy module method")
            except Exception as e:
                logger.info(f"Legacy method failed: {str(e)}")
                # Method 2: Try new client but catch TypeError specifically
                try:
                    # Import the class directly to avoid module-level issues
                    from openai import OpenAI as OpenAIClient
                    # Try with only api_key, no other parameters
                    client = OpenAIClient(api_key=api_key)
                    logger.info("OpenAI client initialized with new method")
                except TypeError as type_error:
                    if 'proxies' in str(type_error):
                        logger.info("Proxies error detected, trying monkey patch")
                        # Method 3: Monkey patch to remove proxies parameter
                        try:
                            import inspect
                            from openai import OpenAI as OpenAIClient
                            
                            # Get the original __init__ method
                            original_init = OpenAIClient.__init__
                            
                            # Create a wrapper that filters out proxies
                            def patched_init(self, *args, **kwargs):
                                # Remove proxies from kwargs if present
                                kwargs.pop('proxies', None)
                                return original_init(self, *args, **kwargs)
                            
                            # Apply the patch
                            OpenAIClient.__init__ = patched_init
                            client = OpenAIClient(api_key=api_key)
                            logger.info("OpenAI client initialized with monkey patch")
                        except Exception as e3:
                            logger.error(f"Monkey patch failed: {str(e3)}")
                            return None
                    else:
                        raise type_error
                except Exception as e2:
                    logger.error(f"New method failed: {str(e2)}")
                    return None
                
            # Verify client is usable
            if client is None:
                logger.error("OpenAI client is None after initialization attempts")
                return None
                
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
            logger.info(f"OpenAI client type: {type(openai_client)}")
            logger.info(f"OpenAI client attributes: {dir(openai_client)}")
            
            try:
                # Try the new responses API first (if available)
                if hasattr(openai_client, 'responses') and hasattr(openai_client.responses, 'create'):
                    logger.info("Using new OpenAI responses API")
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
                    plain_text = response.output[0].content[0].text
                    
                # Try chat completions API (most common) - handle both new and legacy
                elif hasattr(openai_client, 'chat') and hasattr(openai_client.chat, 'completions'):
                    logger.info("Using chat completions API")
                    prompt_text = f"Create a detailed lesson plan for {subject} ({specialty}) for grade {grade}. Duration: {hoursperday} hours/day for {numweeks} weeks in {state}. Focus: {focus}. Additional details: {user_input}"
                    
                    response = openai_client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt_text}],
                        max_tokens=2048,
                        temperature=0.7
                    )
                    plain_text = response.choices[0].message.content.strip()
                
                # Try legacy module-level API calls
                elif hasattr(openai_client, 'ChatCompletion') and hasattr(openai_client.ChatCompletion, 'create'):
                    logger.info("Using legacy ChatCompletion API")
                    prompt_text = f"Create a detailed lesson plan for {subject} ({specialty}) for grade {grade}. Duration: {hoursperday} hours/day for {numweeks} weeks in {state}. Focus: {focus}. Additional details: {user_input}"
                    
                    response = openai_client.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt_text}],
                        max_tokens=2048,
                        temperature=0.7
                    )
                    plain_text = response.choices[0].message.content.strip()
                    
                # Try legacy completions API
                elif hasattr(openai_client, 'completions') and hasattr(openai_client.completions, 'create'):
                    logger.info("Using legacy completions API")
                    prompt_text = f"Create a lesson plan for {subject} ({specialty}) for grade {grade}. Duration: {hoursperday} hours/day for {numweeks} weeks in {state}. Focus: {focus}. Additional details: {user_input}"
                    
                    response = openai_client.completions.create(
                        model="gpt-3.5-turbo-instruct",
                        prompt=prompt_text,
                        max_tokens=2048,
                        temperature=0.7
                    )
                    plain_text = response.choices[0].text.strip()
                    
                # Try very old API format
                elif hasattr(openai_client, 'Completion'):
                    logger.info("Using very old OpenAI API format")
                    prompt_text = f"Create a lesson plan for {subject} ({specialty}) for grade {grade}. Duration: {hoursperday} hours/day for {numweeks} weeks in {state}. Focus: {focus}. Additional details: {user_input}"
                    
                    response = openai_client.Completion.create(
                        model="gpt-3.5-turbo-instruct",
                        prompt=prompt_text,
                        max_tokens=2048,
                        temperature=0.7
                    )
                    plain_text = response.choices[0].text.strip()
                    
                else:
                    logger.error("No compatible OpenAI API method found")
                    raise Exception("OpenAI client has no compatible API methods")
                    
            except Exception as api_error:
                logger.error(f"OpenAI API call failed: {str(api_error)}")
                logger.error(f"Available client methods: {[attr for attr in dir(openai_client) if not attr.startswith('_')]}")
                raise Exception(f"OpenAI API error: {str(api_error)}")
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