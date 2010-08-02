secret_word(word_length)
  file = open ("C:\Documents and Settings\googleuser\My Documents\cssi\unix-words(1)","r")
  word_list = []
  for word in file:
    word = word.strip()
    if len(word) == word_length:
      word_list.append(word)
    file.close()
    if len(word_list) == 0:
      return 0
    else:
      return random.choice(word_list)
