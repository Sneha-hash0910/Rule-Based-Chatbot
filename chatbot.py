import datetime
import random
import re
from intents import greetings, jokes, motivation, facts

def chatbot_response(message):
    #converts user message into lower case
    message = message.lower().strip()

    #greetings
    if message in ["hi", "hello", "hey", "good morning", "good evening", "good afternoon"]:
        return random.choice(greetings)
    
    #introduction
    elif "your name" in message or "who are you" in message:
        return "I am a rule based AI Chatbot developed  using Python."
    elif "creator" in message or "made you" in message:
        return "I was created by Sneha as part of the Codsoft AI Internship."
    
    #feelings
    elif "how are you" in message:
        return "I'm doing great! Thanks for asking. How about you?"
    elif "i am fine" in message:
        return "That's wonderful to hear!"
    elif "i am sad" in message:
        return "I am sorry you're feeling this way, remember every difficult day passes"
    elif "i am happy" in message:
        return "That's great! keep smiling."
    
    #date and time
    elif "time" in message:
        return "current time:" + datetime.datetime.now().strftime("%I:%M %p")  
    elif "date" in message:
        return "Today's date:" + datetime.datetime.now().strftime("%d-%m-%Y") 
    
    #programming
    elif "python" in message:
        return "Python is a popular programming language used for AI, web development, automation and data science."
    elif "java" in message:
        return "Java is a popular object-oriented programming language"
    elif "c++" in message:
        return "C++ is widely used for game develpment and high performance applications."
    
    #AI
    elif "ai" in message or "artificial intelligence" in message:
        return "Artificial intelligence enables computers to perform tasks that normally require human intelligence."
    elif "machine learning" in message or "ml" in message:
        return "Machine Learning is a branch of AI where  systems learn from data."
    
    #calculator
    elif re.fullmatch(r"\d+\s*[\+\-\*/]\s*\d+", message):
        try: 
            return "Answer = " + str(eval(message))
        except:
            return "Invalid calculation"
    
    #motivation    
    elif "motivate" in message or "motivation" in message:
        return random.choice(motivation)
    
    #fun fact
    elif any(word in message for word in ["motivate", "motivation", "inspire", "quote", "motivational"]):
        return random.choice(facts)
    
    #jokes
    elif any(word in message for word in ["joke", "funny", "make me laugh","tell me something funny"]):
        return random.choice(jokes)
    
    #weather
    elif any(word in message for word in ["weather", "temperature", "rain", "sunny"]):
        return "I can't check live weather because I'm rule based, but i hope it's a beautiful day where you are!"
    
    #thanks
    elif "thank" in message:
        return "You're Welcome!"
    
    #sorry
    elif "sorry" in message:
        return "No problem at all!"
    
   #help
    elif "you can do" in message or "help" in message or "you can do" in message:
        return ("you can ask me about:\n"
                "-Time\n"
                "-Date\n"
                "-Python\n"
                "-AI\n"
                "-Tell me a joke\n"
                "-Greetings\n"
                "-My creator\n"
                "-Calculator(Example: 25 + 30)\n"
                "-Motivational quotes\n"
                "-Fun Facts")
    
    #goodbye    
    elif message in ["bye", "exit", "quit"]:
        return "Goodbye! Have a wonderful day"
    
    #default
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see what i can do."