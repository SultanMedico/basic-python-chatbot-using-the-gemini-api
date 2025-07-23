import google.generativeai as genai
from tool import get_gemini_api_key

def initialize_gemini():
    api_key = get_gemini_api_key()
    genai.configure(api_key=api_key)
    print("Gemini API initialized successfully!")

    # --- Temporarily list available models ---
    print("\nAvailable Gemini Models:")
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            print(f"- {m.name} (Supports generateContent)")
    print("---------------------------\n")
    # ----------------------------------------

def main():
    initialize_gemini()
    print("\nWelcome to the Gemini Chatbot! Type 'exit' to quit.")

    # **CHANGE THIS LINE**
    # Use 'gemini-1.5-flash' or 'gemini-1.5-pro' or another supported model from the list above
    model = genai.GenerativeModel('gemini-2.5-pro') # Recommended: 'gemini-1.5-flash' for general use
    # model = genai.GenerativeModel('gemini-1.5-pro') # Alternative: 'gemini-1.5-pro' for more complex tasks

    chat = model.start_chat(history=[])

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! 👋")
            break

        try:
            response = chat.send_message(user_input)
            print(f"Chatbot: {response.text}")
        except Exception as e:
            print(f"Chatbot: An error occurred while generating a response: {e}")
            print("Chatbot: Please try again or type 'exit' to quit.")

if __name__ == "__main__":
    main()