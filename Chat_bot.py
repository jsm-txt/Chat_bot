#Start of code, defining variables and greeting!
print("Welcome to Jose's drink bot!")
from random import choice
response = ""

#Function to output a response to user depending on their input
def get_bot_response(response):

    #List of responses to user
    bot_response_water = ["Good choice!", "Healthy living", "Drink of the intelectuals!", "Stay hydrated"]
    bot_response_tea = ["Leaf juice is king!", "Great choice!", "Good for the soul"]
    bot_response_soda = ["Too much sugar for me", "Not very healthy pal", "Try something else", "Drink some water please"]
    bot_response_juice = ["Not a bad choice", "Apple juice is my favorite", "Juice is power"]
    bot_response_else = ["Surely you joke", "Try something else", "Have you tried water?", "Try water, tea, juice or soda."]

    #If statements to process response and random output
    if response == "water":
        return choice(bot_response_water)

    if response == "tea":
        return choice(bot_response_tea)
    
    if response == "soda":
        return choice(bot_response_soda)
    
    if response == "juice":
        return choice(bot_response_juice)
    
    else:
        return choice(bot_response_else)
        
 
#For loop to keep the program running       
while response != "done":
    response = input("Enter your favorite type of drink: ")
    bot = get_bot_response(response)
    print(bot)