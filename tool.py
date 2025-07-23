import os
from dotenv import load_dotenv

def get_gemini_api_key():
    """
    Loads the Gemini API key from environment variables.
    It's highly recommended to store your API key securely
    and not hardcode it directly in your script.
    """
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables. "
                         "Please set it in a .env file or as an environment variable.")
    return api_key

if __name__ == "__main__":
    # This block is for testing if your API key loads correctly
    try:
        key = get_gemini_api_key()
        print("Gemini API Key loaded successfully (first few chars):", key[:5] + "...")
    except ValueError as e:
        print(f"Error loading API key: {e}")