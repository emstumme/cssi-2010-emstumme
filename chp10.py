# lists Chapter 10 

def add_all(t):
    """Add all the numbers in t and return the sum"""
    total = 0
    for x in t:
        total +=x
    return total

# exercise 4

def is_anagram(s, t):
    """return True if s and t are anagrams"""
    u = list(s)
    v = list(t)
    u.sort()
    v.sort()
    return u == v

    
    

def test_is_anagram():
    if (not is_anagram("posts", "spots"):
        is_anagram("shoes". "grass")) :
        print "is_anagram() is buggy!"

if __name__ == "__main__":
    test_is_anagram()

# random stuff

def mystery(a, b):
    a[0] = 'x'
    b[1] = 'y'
    
