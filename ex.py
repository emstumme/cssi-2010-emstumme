
def hangman():
  print 'time to play hangman'
  secret_word = 'hello'
  guesses = ' '
  turns = 5

  while turns > 0:
    missed = 0
    for letter in secret_word:
      if letter in guesses:
        print letter,
      else:
        print '_',
        missed += 1

    print

    if missed == 0:
      print 'You win!'
      break

    guess = raw_input('Please guess a letter: ')
    guesses += guess

    if guess not in secret_word:
      turns -= 1
      print 'Letter not in Word.'
      print turns, 'more turns'
      if turns == 0:
        print 'The answer is', secret_word
      
