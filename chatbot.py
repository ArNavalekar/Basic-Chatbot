
import nltk
from nltk.chat.util import Chat, reflections

# Define a set of pairs: patterns and corresponding responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?",]
    ],
    [
        r"what is your name?|what your name",
        ["I am a chatbot created using Python. You can call me ChatBot.",]
    ],
    [
        r"how are you?",
        ["I'm doing great, thank you! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no problem!",]
    ],
    [
        r"i'm (.*) doing good|I am fine",
        ["That's great to hear!",]
    ],
    [
        r"how can you help me?",
        ["I can answer questions, chat with you, or provide basic information. What would you like to do?",]
    ],
    [
        r"what you can do?|how you can help me",
        ["I can give your question answers if I can",]
    ],
    [
        r"can you calculate maths?",
        ["Sorry,not now",]
    ],  
    [
        r"who made you?",
        ["Team of programmers made me",]
    ],  
    [
        r"which languages used to built you?",
        ["python,nltk etc.....",]
    ],  
    [
        r"which languages you know?",
        ["what are you asking about the religional language or programming language",]
    ], 
    [
        r"asking about religional language?|religional",
        ["I know Hindi,English,Marathi etc...",]
    ],  
    [
        r"asking about programming language?|programming",
        ["I know python,c,java etc...",]
    ],   
    [
        r"how to remove stress?",
        ["Do what you like,listen song,play games,spent time with favourite person etc...",]
    ], 
    [
        r"thats good|good",
        ["Thanks",]
    ], 
    [
        r"thank you|thanks",
        ["Your most welcome",]
    ],          
    [
        r"quit|bye",
        ["Goodbye! It was nice talking to you.",]
    ],
]

# Create chatbot with pairs and reflections
def chatbot():
    print("Chatbot: Hello! I am a chatbot. You can type 'quit' or 'bye' to end the conversation or to begin chat type 'hi','hello'")
    chatbot = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'quit']:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print("Chatbot:", response)
            else:
                print("Chatbot: Sorry, I don't understand. Can you rephrase?")

if __name__ == "__main__":
    # Download NLTK data required for tokenization
    nltk.download('punkt')
    chatbot()
  
