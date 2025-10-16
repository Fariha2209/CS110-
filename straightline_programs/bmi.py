
#imports necessary libraries
import stdio
import sys

#Reads the command-line inputs
w = float(sys.argv[1])
h = float(sys.argv[2])

#Formula to calculate bmi
bmi = w/(h*h)

stdio.writeln(float(bmi))
