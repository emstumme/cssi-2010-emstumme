# quadratic equation solver
#
# given three constants a, b, and c
# for the quadratic equation a x^2 +b x + c
# return the two roots of the equation as a tuple
#
# Example: qyad(1,3,-4) => (1,-4)
import math 
def quad(a,b,c):
    return (1, -4) # dummy implementation

def quad(a,b,c):
    return (-b +math.sqrt(b**2 - 4*a*c)/2*a),(-b-math.sqrt(b**2-4*a*c)/2*a)

def disc (a,b,c):
    return math.sqrt (b**2 - 4*a*c)

def quad(a,b,c):
    return(-b +disc),(-b-disc)


