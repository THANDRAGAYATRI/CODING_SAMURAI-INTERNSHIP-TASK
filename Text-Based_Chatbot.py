import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

# Define conversations
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hi there! How can I assist you today?",
    "what's the weather like?": "I'm just a text-based chatbot and don't have access to real-time data. Sorry!",
    "default": "I'm not sure I understand. Could you please rephrase or ask another question?"
}

# Function to tokenize and process user input
def preprocess_input(input_text):
    # Tokenize the input text
    tokens = word_tokenize(input_text.lower())
    # Remove stopwords (optional)
    tokens = [token for token in tokens if token not in stopwords.words('english')]
    return tokens

# Function to generate a response
def generate_response(user_input):
    tokens = preprocess_input(user_input)
    for intent, intent_data in conversations.items():
        for pattern in intent_data["patterns"]:
            if pattern in tokens:
                return random.choice(intent_data["responses"])
    # If no pattern matches
    return random.choice(conversations["default"])
# Main interaction loop
print("Chatbot: Hi! How can I assist you today? (type 'exit' to end)")
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = generate_response(user_input)
    print("Chatbot",response)
        