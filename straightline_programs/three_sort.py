
#importing necessary libraries
import stdio
import sys
import math

#Reads command-line inputs 
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])


maximum = max(x, y, z)          #Find the largest value 
minimum = min(x, y, z)          #Find the smallest value

mid = (x + y + z) - (maximum) - (minimum)           #Find the middle value

stdio.writeln(str(minimum) + " " + str(mid) + " " + str(maximum))             #Generates the output in an ascending order