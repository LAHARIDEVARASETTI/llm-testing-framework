
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from models.openai_model import generate_response

prompt = "Hello AI"

response = generate_response(prompt)

print(response)