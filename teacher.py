import json
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    from openai import OpenAI

    # Load environment variables
    load_dotenv()

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    response = client.responses.create(
        prompt={
            "id": os.environ.get("OPENAI_PROMPT_ID"),
            "version": os.environ.get("OPENAI_PROMPT_VERSION"),
            "variables": {
                "subject": "science",
                "specialty": "physical science",
                "grade": "5th",
                "hoursperday": "2",
                "numweeks": "5",
                "state": "California",
                "focus": "education",
            }
        },
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Can you generate a plan no more than 100 words."
                    }
                ]
            }
        ],
        reasoning={},
        max_output_tokens=2048,
        store=True
    )
    # Print the structured JSON response
    print(json.dumps(response.to_dict(), indent=4))