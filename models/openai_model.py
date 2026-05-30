from openai import OpenAI
import os
from config.settings import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)

def generate_response(prompt):

    response = client.chat.completions.create(
        MODEL_NAME = os.getenv("OPENAI_MODEL"),
        

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content