# quadratic equation solver
#
# given three constants a, b, and c
# for the quadratic equation a x^2 +b x + c
# return the two roots of the equation as a tuple
#
# Example: qyad(1,3,-4) => (1,-4)
import math 


def quad(a,b,c):
   disc_squared = b*b - 4 * a * c
   # this is the place to check for a negative number
   if disc_squared <0:
       print "oh no! negative argument to square root"
       return 
   disc = math.sqrt(disc_squared)
   one= ((-b)+ disc) / (2 * a)
   two= ((-b)- disc) / (2 * a)
   return one, two 




