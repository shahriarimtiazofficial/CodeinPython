import random


responses = {
    "creator": ["Shahriar Imtiaz!", "Imtiaz!", "Shahriar"],
    "hello": ["Hello there!", "Hi!", "Hello! How can I help you?"],
    "how are you": ["I am just a bot, but I'm here to help!", "Doing great! What about you?"],
    "what is your name": ["I'm a simple imibot!", "You can call me imibot."],
    "bye": ["Goodbye!", "See you later!", "It was nice talking to you!"],
    "creator": ["Shahriar Imtiaz!", "Imtiaz!", "Shahriar"],
    "more" :{"will be updated"},
}

print("Imibot: Hello! Type 'bye' to exit.")


while True:
    user_input = input("You: ").lower() 
    
    
   
    if user_input == "bye":
        print("Imibot: Goodbye!")
        break  

    found_response = False 
    for key in responses:
        if key in user_input:
        
            print("Imibot:", random.choice(responses[key])) 
            found_response = True
            break  
 
    if not found_response:
        print(" Imibot: I am sorry, I don't understand that.")

