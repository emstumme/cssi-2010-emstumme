# factorial function
#
#return the factorial of n. 
# fact(m)=> n! => n* (n-1) + (n-2) *...* 1
# fact(n) = n n * fact(n-1)
# fact(5) = 5 * fact(4)

#interative
def factier(n):
    print "called with", n 
    while n > 1:
        print "in while loop, n =" , n 
        n = (n - 1)
        answer = ... n ...
    return answer # 5 * 4 * 3 * 2 * 1
    
# recursive
def factdoc(n):
    print n
    if n == 1:
        return 1
    partial = fact(n-1)
    print n - 1, " => ", partial
    return n * partial

def fact(n):
    while n => 1:
        return n * fact(n - 1)
        
