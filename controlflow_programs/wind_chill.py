#Importing necessary libraries
import stdio
import sys
import math

#assigns variable t and v the input values
t = float(sys.argv[1])
v = float(sys.argv[2])

#formula to compute w
w = 35.74 + 0.6215*t + (0.4275*t - 35.75) * v**0.16

#Starts an if statement
if t > 50:                     #Checks if value t is greater than or less than 50 
    stdio.writeln("Value of t must be <= 50 F")         
elif v <= 3:                   #Checks if value of v is greater than or less than 3
    stdio.writeln("Value of v must be > 3 mph")
else:                          #If both the conditions are met, computes the value of w using the input values
    w = 35.74 + 0.6215*t + (0.4275*t - 35.75) * v**0.16             
    stdio.writeln(str(w))      #Writes the computed value of w


    