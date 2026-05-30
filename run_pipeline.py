
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.openai_model import generate_openai_response
print("Done")

prompt = "Hello AI"

response = generate_openai_response(prompt)

print(response)