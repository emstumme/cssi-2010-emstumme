# factorial function
#
#return the factorial of n. 
# fact(m)=> n! => n* (n-1) + (n-2) *...* 1
# fact(n) = n n * fact(n-1)
# fact(5) = 5 * fact(4)

#interative

# factorial function for using loop
def factfor(n):
    answer = 1
    for x in range(1, n):
        answer = answer * (x * 1) 
    return answer

def factier(n):
    answer = 1
    while n > 1:
        answer = answer * n 
        n = (n - 1)
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
    while n == 1:
        return n * fact(n - 1)
        
