
# defines hangman, secret word, and amount of turns

import random
import string

def hangman():
  print 'time to play hangman'
  secret_word = 'hello'
  guesses = ' '
  turns = 5

#shows spaces for word
  while turns > 0:
    missed = 0
    for letter in secret_word:
      if letter in guesses:
        print letter,
      else:
        print '_',
        missed += 1

    print
    
#defines when you win
    if missed == 0:
      print 'You win!'
      break
    
#ask for letters 
    guess = raw_input('Please guess a letter: ')
    guesses += guess
    
# defines what happens when guess is wronf
    if guess not in secret_word:
      turns -= 1
      print 'Letter not in Word.'
      print turns, 'more turns'
      if turns == 0:
        print 'The answer is', secret_word

         



             

