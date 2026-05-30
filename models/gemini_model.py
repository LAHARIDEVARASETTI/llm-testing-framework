import google.generativeai as genai

from config.settings import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

def generate_response(prompt):

    response = model.generate_content(prompt)

    return response.text