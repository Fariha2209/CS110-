
#importing all necessary libraries
import stdio
import sys
import math

#Reads the command-line inputs
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

#Changes the values to radians
x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

#Circle Formula for calculation
d = 6359.83 * (math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)))

#Generates the calculated value as an output
stdio.writeln(d)

