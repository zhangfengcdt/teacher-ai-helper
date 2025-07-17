import os
from flask import Flask, request, render_template
from openai import OpenAI

app = Flask(__name__)

# OpenAI client setup
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        subject = request.form.get("subject")
        specialty = request.form.get("specialty")
        grade = request.form.get("grade")
        hoursperday = request.form.get("hoursperday")
        numweeks = request.form.get("numweeks")
        state = request.form.get("state")
        focus = request.form.get("focus")
        format = request.form.get("format")  # New variable
        user_input = request.form.get("user_input")

        # Send data to OpenAI endpoint
        response = client.responses.create(
            prompt={
                "id": "pmpt_685eb5f872c4819796577ec226efeade0e49ce44769c0c7e",
                "version": "5",
                "variables": {
                    "subject": subject,
                    "specialty": specialty,
                    "grade": grade,
                    "hoursperday": hoursperday,
                    "numweeks": numweeks,
                    "state": state,
                    "focus": focus,
                    "format": format  # Include the new variable
                }
            },
            input=[{"role": "user", "content": user_input}],
            reasoning={},
            max_output_tokens=2048,
            store=True
        )

        # Extract plain text from the response
        plain_text = response.output[0].content[0].text

        # Render the response on the page
        return render_template("index.html", response=plain_text)

    return render_template("index.html", response=None)

if __name__ == "__main__":
    app.run(debug=True)