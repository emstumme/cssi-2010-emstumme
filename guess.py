# guessing game
#
# >>>> guessee(100)
# I have a number betwenn 1 and 100.
# your guesas? 23
# higher
# your guess? 34
# correct
# >>>>

import random

def guessee(maxvalue):
    """ Thinks of a number between 1 and maxvalue, inclusive,
and responds to guesses about what the number is"""
    answer = random.randint(1, maxvalue)
    guessRight = False
    guess = raw_input("Please enter your guess")
    int(guess)
    while guessRight == False:
        n = answer
        g = guess
    
        if n > g:
            print ("Higher")
            guess = input("Guess Higher")
        elif g > n:
            print ("Lower")
            guess = input("Guess Lower")
    else: 
            print ("You win" )



def guesser(maxvalue)
    """ Guesses the user's number between 1 and max value"""
    low = 1
    high = maxva;ue
    while True:
    guess = random.randint(low,maxvalue)
    print "I guess " + str(guess)
    response = raw_input("Did i get it?")
    if response == "yes":
        print "woo hoo"
    elif response == "higher"
        low = guess + 1
    elif response == "lower":
        high = guess - 1
    else:
        print "hmmm, I don't understand '" + response + "'"
        

    
