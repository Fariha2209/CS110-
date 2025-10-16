#imports all the necessary libraries 
import stdio
import sys
import math

#assigns the command-line argument float value
a = float(sys.argv[1])            
b = float(sys.argv[2])
c = float(sys.argv[3])

discriminant = b*b - (4 * a * c)         #formula to calculate discriminant


if a == 0:                                                               #if a equals 0, equation is not quadratic
    stdio.writeln("Value of a must not be 0")                            #displays an error message
elif  discriminant < 0:                                                  #if a is smaller than 0, root is imaginary  
    stdio.writeln("Value of discriminant must not be negative")          #displays an error message         
else: 
    r1 = (- b + math.sqrt(discriminant)) / (2*a)                         #defines qudratic formula for the value
    r2 = (- b - math.sqrt(discriminant)) / (2*a)
    stdio.writeln(str(r1) + " " + str(r2))                                #writes the value in the given format
        



