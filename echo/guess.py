# guessing game
#
# >>> guessee(100)
# I have a number between 1 and 100.
# your guess? 23
# higher!
# >>>
# your guess? 34
# correct
# >>>

import random

def get_number(maxvalue):
    """create a game state based on maxvalue"""
    return random.randint(1, maxvalue)

def check_guess(number, guess):
    """return WON, LOW, or HIGH based on guess"""
    if number == guess:
        return (False, "you won")
    elif number < guess:
        return (True, "too high")
    else:
        return (True, "too low")

def one_turn(number, request):
    """respond to the user's request"""
    if not request:
        return (False, "goodbye")
    else:
        return check_guess(number, int(request)) 
        

    
