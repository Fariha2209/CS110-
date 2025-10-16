
#Imports all the necessary libraries
import stdio
import sys
import math

#Reads command-line inputs 
lmbda = float(sys.argv[1]) 
t = float(sys.argv[2])

p = math.exp(-lmbda * t)  #Formula for calculating the output results

#Generates the calculated result
stdio.writeln(p)

