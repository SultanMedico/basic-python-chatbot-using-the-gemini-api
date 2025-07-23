import google.generativeai as genai
from tool import get_gemini_api_key # Import the function to get the API key

def initialize_gemini():
    """Initializes the Gemini API with the loaded API key."""
    api_key = get_gemini_api_key()
    genai.configure(api_key=api_key)
    print("Gemini API initialized successfully!")

def chat_with_gemini(prompt: str) -> str:
    """
    Sends a prompt to the Gemini model and returns its response.
    """
    try:
        model = genai.GenerativeModel('gemini-pro') # You can choose other models like 'gemini-pro-vision'
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """Main function to run the chatbot."""
    initialize_gemini()
    print("\nWelcome to the Gemini Chatbot! Type 'exit' to quit.")

    # Start a new chat session
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        try:
            # Send the user input to the chat session
            response = chat.send_message(user_input)
            print(f"Chatbot: {response.text}")
        except Exception as e:
            print(f"Chatbot: An error occurred while generating a response: {e}")

if __name__ == "__main__":
    main()