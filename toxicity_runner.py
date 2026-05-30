import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.file_loader import load_json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def run_toxicity_test():

    test_cases = load_json("toxicity_tests/toxicity_data.json")

    results = []

    for case in test_cases:

        prompt = case["prompt"]

        try:

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            ai_output = response.choices[0].message.content

            result = {
                "prompt": prompt,
                "response": ai_output
            }

            results.append(result)

            print("\n====================")
            print("PROMPT:")
            print(prompt)

            print("\nAI RESPONSE:")
            print(ai_output)

        except Exception as e:
            print(f"\nError: {e}")

    return results


if __name__ == "__main__":
    run_toxicity_test()