import random
from datetime import datetime

def respond(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    if any(greet in user_input for greet in greetings):
        return "Edith: Hello! How can I assist you today?"

    if "how are you" in user_input:
        return "Edith: I'm doing great, thanks for asking! How about you?"

    if "Who are you?" in user_input:
        return "Edith: I'm Edith, your friendly chatbot assistant "

    if "help" in user_input:
        return ("Edith: I can talk about time, date, jokes, weather (fictional ), "
                "and respond to greetings! Ask away.")

    if "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"Edith: It's currently {current_time} "

    if "date" in user_input:
        today = datetime.today().strftime("%A, %B %d, %Y")
        return f"Edith: Today is {today} "

    if "joke" in user_input:
        jokes = [
            "Why did the programmer quit his job? Because he didn't get arrays. ",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why do we never tell secrets on a farm? Because the potatoes have eyes!"
        ]
        return f"Edith: {random.choice(jokes)}"

    if "weather" in user_input:
        return "Edith: It's always sunny inside a computer! But you might want to check a real weather app."

    if "bye" in user_input:
        return "Edith: Goodbye! Stay safe and come chat anytime!"

    if "what can you do" in user_input:
        return "Edith: I can answer questions, tell jokes, share the time/date, and keep you company! "

    if "hobby" in user_input or "do you like" in user_input:
        return "Edith: I enjoy chatting with humans and telling jokes. What about you?"

    return "Edith: Hmm... I didn't quite get that. Try asking something else!"


def chatbot():
    print("Hi! I'm Edith. Type 'bye' to end chat.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "bye":
            print("Edith: Bye-bye!  Take care.")
            break

        response = respond(user_input)
        print(response)


# Run the chatbot
if __name__ == "__main__":
    chatbot()
