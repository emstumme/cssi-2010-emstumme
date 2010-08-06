# Exercises from Chapter 8: Strings

one = 'emily'
two = 'stumme'

def fullname(first, last):
    return first + ' ' + last

def fullname2(first, last):
    return '%s %s' % (first, last)

# Exercise 1
# Write a  funstion that takes a string as an argument and displays
# the letters backwards, one per line.

def backwards(s):
    """print the letters of s backwards, one per line"""
    length = len(s)
    index = length - 1
    for c in s:
        print s[index]
        index = index-1
   
def backwards1(s):
    """print the letters of s vackwards, one per line"""
    length = len(s)
    index = length - 1
    while index >=0:
        c  = s[index]
        index = index -1
        print c
        
# Exercise 2

def ducklings():
    """print the names of the ducklings"""
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'Q' or letter == 'O':
            print letter + "u" + suffix
        else:
            print letter + suffix

# Exercise 4

def find(word, letter):
    """Return the index of a certain letter"""
    index = 0
    while index < len(word):
        if word[index] -- letter:
            return index
        index = index + 1
        return -1

#Exercise 12

    def rotate_letter(letter,shift) :
        """Return the letter shifted by the value"""
        decimal = ord(letter)
        shifted = decimal + shift
        if shifted > 126:
            shifted = shifted - 94
        elif shifted < 32:
            shifted = shifted + 94
        return chr(shifted)

    def rotate_word(original, shift):
        """Return a string where each letter in original is shifted
           For example, rotate_word("hello",3) => "khoor"."""
        rotated = ""
        for c in original:
            rot = rotate_letter(c, shift)
            rotated = rotated + rot
        print rotated

    def test_rotate_letter():
        if (rotate_letter(' ', -1) != '~' or
            rotate_letter('~', 1) != ' '):
            print "rotate_letter is buggy!"

    
