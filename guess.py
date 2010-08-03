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

def check_number(user_guess):
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
        check_guess(number, int(request)) 
        

    
def guessee_iter(number):
    """play the guessing game with the number"""
    guess = number + 1
    while not guess == number:
        response = raw_input("Your guess? ")
        guess = int(response)
        if guess < number:
            print "Too low"
        elif guess > number:
            print "Too high"
        else:
            print "You got it!"

def guessee_rec(number):
    """play the guessing game with the number"""
    response = raw_input("Your guess? ")
    guess = int(response)
    if guess < number:
        print "Too low"
        guessee_rec(number)
    elif guess > number:
        print "Too high"
        guessee_rec(number)
    else:
        print "You got it!"
        
def guessee(maxvalue):
    """Thinks of a number between 1 and maxvalue, inclusive,
and responds to guesses about what the number is"""
    print "I am thinking of a number from 1 to " + str(maxvalue) + "."
    print "Guess, and I will tell you when you get it right!"
    number = random.randint(1, maxvalue)
    guessee_rec(number)


# >>> guesser(100)
# is it 50? higher
# is it 60? lower
# is it 53? yes
# i win!
# >>>

def guesser_iter(maxvalue):
    """Guesses the user's number between 1 and maxvalue"""
    low = 1
    high = maxvalue
    response = ""
    while not response == "yes":
        # here's the stuff that I repeat later
        print low, high
        guess = random.randint(low, high)
        print "I guess " + str(guess)
        response = raw_input("Did I get it? ")
        if response == "yes":
            print "woo hoo"
        elif response == "higher":
            low = guess + 1
        elif response == "lower":
            high = guess - 1
        else:
            print "hmmm, I don't understand '" + response + "'"

def guesser_rec(low, high):
    """Guess a number between low and high"""
    guess = random.randint(low, high)
    print "I guess " + str(guess)
    response = raw_input("Did I get it? ")
    if response == "yes":
        print "woo hoo"
    elif response == "higher":
        guesser_rec(guess + 1, high)
    elif response == "lower":
        guesser_rec(low, guess - 1)
    else:
        print "hmmm, I don't understand '" + response + "'"
        guesser_helper(low, high)

def guesser(maxvalue):
    """Guesses the user's number between 1 and maxvalue"""
    guesser_rec(1, maxvalue)


# >>> game(100)
# Think of a number between 1 and 100. I will think of one, too.
# We will take turns guessing.
# Your guess? 50
# Too low! I guess 23? higher
# Your guess? ...
# ...

# There are five elements to the state of the game:
#   number  - the number that the user is guessing
#   low     - the lower bound for the computer's guesses
#   high    - the upper bound for the computer's guesses
#   userwin - has the user won the game?
#   compwin - has the computer won the game?
#
# Internally, we represent the state with a dictionary, but clients
# of this API do not know that.
#
# We will use this API for both the recursive and iterative versions.

def create_state(number, maxvalue):
    """return an initial game state with the number and the upper bound"""
    return { "number" : number,
             "low" : 1,
             "high" : maxvalue,
             "userwin" : False,
             "compwin" : False }

def get_number(state):
    """return the number that the user is trying to guess"""
    return state["number"]

def get_low(state):
    """return the lower bound of the computer's guesses"""
    return state["low"]

def get_high(state):
    """return the upper bound of the computer's guesses"""
    return state["high"]

def get_compwin(state):
    """True iff the computer has won, False otherwise"""
    return state["compwin"]

def get_userwin(state):
    """True iff the user has won, False otherwise"""
    return state["userwin"]

def set_low(state, low):
    """Set the computer's lower bound"""
    state["low"] = low

def set_high(state, high):
    """Set the computer's upper bound"""
    state["high"] = high

def set_compwin_true(state):
    """Set the compwin condition to True"""
    state["compwin"] = True

def set_userwin_true(state):
    """Set the userwin condition to True"""
    state["userwin"] = True

# The game playing program. The following code uses the API functions
# defined above, but does not know that the state is implemented as
# a dictionary.
#
# This is a recursive solution. Whose turn it is is determined by the
# calls between user_rec and computer_rec. They pass the state back and
# forth, and each must test to see if the game is over.
#
# Study the differences between this and the iterative version.

def game_rec(maxvalue):
    """play the guessing game with the computer"""
    print ("Think of a number between 1 and " +
           str(maxvalue) +
           ". I will think of one, too.")
    print "We will take turns guessing."
    number = random.randint(1, maxvalue)
    state = create_state(number, maxvalue)
    computer_rec(state)

def user_rec(state):
    """play the guessing game with the number"""
    number = get_number(state)
    compwin = get_compwin(state)
    userwin = get_userwin(state)
    if userwin and compwin:
        print "game over"
    elif userwin:
        computer_rec(state)
    else:
        response = raw_input("                       Your guess? ")
        guess = int(response)
        if guess < number:
            print "                       Too low"
            computer_rec(state)
        elif guess > number:
            print "                       Too high"
            computer_rec(state)
        else:
            print "                       You got it!"
            set_userwin_true(state)
            computer_rec(state)

def computer_rec(state):
    """Guess a number between low and high"""
    low = get_low(state)
    high = get_high(state)
    compwin = get_compwin(state)
    userwin = get_userwin(state)
    if userwin and compwin:
        print "game over"
    elif compwin:
        user_rec(state)
    else:
        guess = random.randint(low, high)
        print "I guess " + str(guess)
        response = raw_input("Did I get it? ")
        if response == "yes":
            print "woo hoo"
            set_compwin_true(state)
            user_rec(state)
        elif response == "higher":
            set_low(state, guess + 1)
            user_rec(state)
        elif response == "lower":
            set_high(state, guess - 1)
            user_rec(state)
        else:
            print "hmmm, I don't understand '" + response + "'"
            computer_rec(state)

# Here is an iterative version of the program. It also uses the state
# API. Notice how most of the code is the same, except that it uses
# a while loop instead of recursion.
#
# The iterative version needs another state variable, which is whose
# turn it is. In the recursive version, we track turns *implicitly*
# through the function calls. In the iterative version, we track turns
# *explicitly* through a separate state variable, "is_user_turn", which
# alternates between True and False.
#
# Notice the condition for the while loop. I decided to make a separate
# function for this, as it is a lot clearer that way.
#
# Notice that I still have separate functions for the user and the computer,
# even though I could have put them into one monolithic function. In
# computer programming, "monolithic" => "bad". Separate functions makes
# the code much clearer, and allows me to test each one separately.
#
# There is still one recursive call in this program. Can you find it?

def game_over(state):
    """return true if the game is over"""
    return get_userwin(state) and get_compwin(state)

def game_iter(maxvalue):
    """play the guessing game with the computer"""
    print ("Think of a number between 1 and " +
           str(maxvalue) +
           ". I will think of one, too.")
    print "We will take turns guessing."
    number = random.randint(1, maxvalue)
    state = create_state(number, maxvalue)
    is_user_turn = False
    while not game_over(state):
        if is_user_turn:
            user_iter(state)
        else:
            computer_iter(state)
        is_user_turn = not is_user_turn

def user_iter(state):
    """play the guessing game with the number"""
    number = get_number(state)
    userwin = get_userwin(state)
    if not userwin:
        response = raw_input("                       Your guess? ")
        guess = int(response)
        if guess < number:
            print "                       Too low"
        elif guess > number:
            print "                       Too high"
        else:
            print "                       You got it!"
            set_userwin_true(state)

def computer_iter(state):
    """Guess a number between low and high"""
    low = get_low(state)
    high = get_high(state)
    compwin = get_compwin(state)
    if not compwin:
        guess = random.randint(low, high)
        print "I guess " + str(guess)
        response = raw_input("Did I get it? ")
        if response == "yes":
            print "woo hoo"
            set_compwin_true(state)
        elif response == "higher":
            set_low(state, guess + 1)
        elif response == "lower":
            set_high(state, guess - 1)
        else:
            print "hmmm, I don't understand '" + response + "'"
            computer_iter(state)
