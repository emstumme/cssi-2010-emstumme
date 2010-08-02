import random
import guessstate 

def game_rec(maxvalue):
    """play the guessing game with the computer"""
    print ("Think of a number between 1 and " +
           str(maxvalue) +
           ". I will think of one, too.")
    print "We will take turns guessing."
    number = random.randint(1, maxvalue)
    state = gs.create_state(number, maxvalue)
    computer_rec(state)

def user_rec(state):
    """play the guessing game with the number"""
    number = state.get_number()
    compwin = state.get_compwin()
    userwin = state.get_userwin()
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
            gs.set_userwin_true(state)
            computer_rec(state)

def computer_rec(state):
    """Guess a number between low and high"""
    low = state.get_low()
    high = state.get_high()
    compwin = state.get_compwin()
    userwin = state.get_userwin()
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
            gs.State.set_compwin_true(state)
            user_rec(state)
        elif response == "higher":
            gs.State.set_low(state, guess + 1)
            user_rec(state)
        elif response == "lower":
            gs.set_high(state, guess - 1)
            user_rec(state)
        else:
            print "hmmm, I don't understand '" + response + "'"
            computer_rec(state)

