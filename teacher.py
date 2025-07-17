import json

if __name__ == '__main__':
    from openai import OpenAI

    client = OpenAI()

    response = client.responses.create(
        prompt={
            "id": "pmpt_685eb5f872c4819796577ec226efeade0e49ce44769c0c7e",
            "version": "6",
            "variables": {
                "subject": "science",
                "specialty": "physical science",
                "grade": "5th",
                "hoursperday": "2",
                "numweeks": "5",
                "state": "California",
                "focus": "education",
                "format": "text"
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
            },
            {
                "id": "msg_6862a4139b108192992317c89b52c3c9042f0963f730f8f1",
                "role": "assistant",
                "content": [
                    {
                        "type": "output_text",
                        "text": "**5-Week Physical Science Plan (Grade 5, CA Standards):**  \nStudents will explore matter, energy, force, and motion through hands-on labs, group experiments, and interactive games. Each week introduces new concepts with daily activities, including vocabulary review, experiments (like building simple circuits or observing chemical changes), and formative quizzes. Differentiation includes guided notes and extension tasks. Projects reinforce content knowledge. Assessment via weekly quizzes and a final project presentation ensures mastery. All lessons align to California NGSS.  \n\n**Clarifying question:**  \nWould you like a specific project example or focus on a particular physical science topic (e.g., energy or matter)?"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Can you generate a plan no more than 100 words. Don't ask anymore questions."
                    }
                ]
            },

        ],
        reasoning={},
        max_output_tokens=2048,
        store=True
    )
    # Print the structured JSON response
    print(json.dumps(response.to_dict(), indent=4))