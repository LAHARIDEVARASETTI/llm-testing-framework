from config.ai_config import (
    OPENAI_API_KEY,
    GEMINI_API_KEY,
    DEFAULT_PROVIDER
)

def get_provider():

    if DEFAULT_PROVIDER == "openai":
        return {
            "provider": "openai",
            "api_key": OPENAI_API_KEY
        }

    elif DEFAULT_PROVIDER == "gemini":
        return {
            "provider": "gemini",
            "api_key": GEMINI_API_KEY
        }

    else:
        raise ValueError("Unsupported provider")