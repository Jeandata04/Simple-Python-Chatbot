import json
import random

# Load responses
with open("responses.json", "r") as file:
    responses = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "I'm not sure how to respond to that yet."

print("Chatbot: Hello! Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break

    response = get_response(user_input)
    print("Chatbot:", response)