#imports all the necessary libraries
import stdio
import sys
import math
import stdrandom

#takes command-line inputs
a = int(sys.argv[1])
b = int(sys.argv[2])

#generates three random floating points between the range (a, b)
x1 = stdrandom.uniformFloat(a, b)
x2 = stdrandom.uniformFloat(a, b)
x3 = stdrandom.uniformFloat(a, b)

µ = (x1 + x2 + x3)/3       #calculates mean 
var = ((x1 - µ) * (x1 - µ) + (x2 - µ) * (x2 - µ) + (x3 - µ) * (x3 - µ))/3          #calculates variance
deviation = math.sqrt(var)          #calculates standard deviation
 

stdio.writeln(str(µ) + " " + str(var) + " " + str(deviation))       #outputs the results in the setting mean, variance and standard deviation
