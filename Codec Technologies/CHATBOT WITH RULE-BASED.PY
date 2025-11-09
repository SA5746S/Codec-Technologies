# Rule-Based Chatbot Example
print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if "bye" in user_input:
        print("Chatbot: Goodbye! Have a nice day 😊")
        break

    # Greetings
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hi there! How can I help you today?")

    # Asking about name
    elif "your name" in user_input:
        print("Chatbot: I'm ChatGPT Jr., your simple rule-based chatbot 🤖")

    # Asking about weather
    elif "weather" in user_input:
        print("Chatbot: I can’t check the weather yet, but it looks sunny in your code world! ☀️")

    # Asking about time
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Chatbot: The current time is {current_time}")

    # Asking about help
    elif "help" in user_input:
        print("Chatbot: I can answer basic questions like greetings, time, or weather!")

    # Default response
    else:
        print("Chatbot: Sorry, I didn't understand that. Try asking something else.")
