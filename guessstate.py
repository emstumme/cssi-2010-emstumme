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
