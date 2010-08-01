# hangman 

def hangman():
    print 'Hangman'
    secret_word = 'hello'
    guesses = '_'
    turns = 7

    while turns >0:
        missed = 0
        for letter in secret_word:
            if letter in guesses:
                print letter
            else:
                print '_'
                missed +=1

     guess = raw_input("Please enter a letter: ")
     guess += guesses

     if guess not in secret word:
         turns -=1
         print 'Letter not in Word'
         print ' Turns left'
     else guess not in secret word:
         turns == 0
             print 'The answer is', secret_word

         



             

