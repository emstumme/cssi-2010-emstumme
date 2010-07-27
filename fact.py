# factorial function
#
#return the factorial of n. 
# fact(m)=> n! => n* (n-1) + (n-2) *...* 1
# fact(n) = n n * fact(n-1)
# fact(5) = 5 * fact(4) 

def fact(n):
    if n == 0:
        return 1
    return n * fact(n- 1)

def factone(n):
    return 1 
        
