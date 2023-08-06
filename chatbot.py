def chatbot_response(user_input):
    # Convert user input to lowercase for easier comparison
    user_input = user_input.lower()

    # Define the rules and corresponding responses
    if 'hello' in user_input:
        return "Hello! How can I assist you?"
    elif 'how are you' in user_input:
        return "I'm just a chatbot, but thanks for asking!"
    elif 'what is your name' in user_input:
        return "I am a simple rule-based chatbot."
    elif 'goodbye' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

def main():
    print("Chatbot: Hello! How can I assist you? (type 'goodbye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'goodbye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = chatbot_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
