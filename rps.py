# rock scissors paper
#
# judge a rock paper scissors contest
#
# one? rock
#two? scissors
# one wins

def rsp():
    r = "rock"
    s = "scissors"
    p = "paper"
    first = raw_input (" Player one Enter a word ")
    second = raw_input ("Player two Enter a word ")
    if (first == r and second == s) or (first == s and second == p) or (first == p and second == r):
        print "Player One Wins!"
    elif (first == second):
        print "It is a tie!"
    else:
        print "Player Two Wins"
    
def get_choice():
    x = raw_input("what does " = name1 + "choose?")
    if x == "rock" or x == "scissors" x == "paper":
        return x
    print "you need to enter rock , paper or scissors:",x
    get_choice()
