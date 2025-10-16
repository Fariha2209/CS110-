#imports all necessary libraries
import stdio
import sys
import math

#Reads the command-line inputs
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

#Sets expr to check for conditions(sum of two sides is >= third side) to see if it is a triangle
expr = (x + y >= z) and (y + z >= x) and (x + z >= y)

#Generates output based on whether conditions show true or false 
stdio.writeln(expr)
