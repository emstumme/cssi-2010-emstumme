# experiments

def square(x):
    return x * c

def squares(n):
    """return a list of the first n squares"""
    results = []
    for x in range(n):
        sq = square(x)
        results.append(sq)
    return results

def newsquares(n):
    """return a list of the first n squares"""
    # list comprehensions
    return [x * x for x in range(n)]

# sets
s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])
s3 = s1.intersection(s2)
s4 = s1.union(s2)
s5 = s1.difference(s2)
s6 = s1.symmetric_difference(s2)

#comprehension
c1 = [x for x in range(5)]
c2 = [x for x in range(5) if x > 3]
c3 = [ (x,y) for x in range(3) for y in "cat"]
c4 = [x for x in "goodbye" if x > 'f' if x < 'v']
c5 = set(x for x in "goodbye" if x > 'f' if x < 'v')
c6 = {x : "cat"[x] for x in range(3)}

# looping constructs
print 'elements of c2:'
for x in c3: print x
print 'elements of c5:'
for x in c5: print x
print 'elements of c6:'
for a, b, in c6.iteritems(): print a,b
print 'elements of a list'
for x in "goodbye" : print x
print 'enumerate elemnts of a list'
for i, x in enumerate("goodbye"): print i, x
print 'enumerate the keys and values'
for i, (k, v) in enumerate(c6.iteritems()): print i, k, v

# other sequence functions
u1 = map(square, range(4))

def between(a,b,c):
    """return True iff a < b <c"""
    return a < b and b < c

u2 = map(between, [1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7])

def getletter(i, s):
    """return the ith letter of s"""
    return s[i]

u3 = map(getletter,
         [2,4,1],
         ["hello", "goodbye", "san francisco"]

indices = [2,4,1]
strings = ["hello", "goodbye", "san francisco"]

u4 = []
for x in range(len(indices)):
         c = getletter(indices[x], strings[x])
         u4.append(c)

u5 = map(getletter, indices, strings)

u6 = [getletter(indices[x], strings[x])
      for x in range(len(indices))]

def odd(x):
         return x % 2 == 1

u7 = filter(odd, range(10))

def add(x,y): return x + y 

u8 = reduce(add, range(10))
u9 = reduce(add, filter(odd, range(10))

a, b = divmod(34, 12)

            d = { i : "goodbye"[i] for i in range(len("goodbye")) )
         
