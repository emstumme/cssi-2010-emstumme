# square.py - print the square of a number

import sys # contains system-related stuff

def square(x):
    return x * x 

if __name__=="__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        print square(int(sys.argv[1]))
    else:
        print 'usage:', sys.argv[0], 'number'
    

