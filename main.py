#Rule Base AI ChatBot

import datetime
import time
name = input("Plz, Enter your name (sir/mam) : ")
presentHour = datetime.datetime.now().hour

if 5<= presentHour <= 11:
    print("Good Morning " , name)
if 11<= presentHour <=17:
    print("Good Afternoon", name)
if 17 <= presentHour <=20:
    print("Good evening", name)
else:
    print("Good Night ", name)

print("Welcome to your  ChatBot")
print("You can asked me basic question , Type 'bye' to exit from the bot ")

# Chatbot memory creation [dictionary of responses]

responses = {
   
    "hi": "Hello! 👋",
    "hello": "Hi there!",
    "hey": "Hey, how can I help you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "name": "Mera naam ChatBot hai. 😊",
    "bye": "Bye! Milte hain phir. 👋",
    "thanks": "You're welcome!",
    "thank you": "Glad I could help!",
    "what is your purpose": "Main yahan madad karne ke liye hoon!",
    "help": "Aap kis cheez mein madad chahte hain?",
    "who created you": "Mujhe ek smart developer ne banaya hai.",
    "joke": "Kya aap ek chutkula sunna chahenge? 😂",
    "weather": "Mausam ka haal check karne ke liye weather app ya website dekhein.",
    "time": "Main waqt to nahi bata sakta, par aap apne device ka clock check kar sakte hain.",
    "date": "Aaj ki tarikh apne phone ya computer se check karo.",
    "default": "Sorry, main samajh nahi paya. 😅"
}

#methond to get reposne of chatbot
def getResponseofbot(userQuestion) :
    userQuestion= userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "I dont know this thinks. sorry..., i will learn that soon."    

#take user input

while True:
    userInput = input("Please asked you question: ")
    reply = getResponseofbot(userInput)
    print("Bot Response : ", reply)

    if "bye" in userInput.lower():
        break