print("Welcome to Jose's food bot!")

from random import choice
response = ""

def get_bot_response(response):

    bot_response_water = ["Good choice!", "Healthy living", "Drink of the intelectuals!", "Stay hydrated"]
    bot_response_tea = ["Leaf juice is king!", "Great choice!", "Good for the soul"]
    bot_response_soda = ["Too much sugar for me", "Not very healthy pal", "Try something else"]
    bot_response_juice = ["Not a bad choice", "Apple juice is my favorite", "Juice is power"]
    bot_response_else = ["Surely you joke", "Try something else", "Have you tried water?", "Drink some water please", "Get hydrated"]

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
        
 
        
while response != "done":
    response = input("Enter your favorite type of drink: ")
    bot = get_bot_response(response)
    print(bot)