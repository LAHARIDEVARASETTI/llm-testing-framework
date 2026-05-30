from models.mock_model import generate_response as mock_response

from models.gemini_model import generate_response as gemini_response

from models.openai_model import generate_response as openai_response

import os

DEFAULT_MODEL = os.getenv(
    "DEFAULT_MODEL",
    "mock"
)

def get_model_response(prompt):

    if DEFAULT_MODEL == "gemini":

        return gemini_response(prompt)

    elif DEFAULT_MODEL == "openai":

        return openai_response(prompt)

    return mock_response(prompt)