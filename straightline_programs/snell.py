
#importing the necessary libraries
import stdio
import sys
import math

#Reads the command-line argument
theta1 = float(sys.argv[1])     
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])
 
theta1 = math.radians(theta1)                        #changes the value to radians
theta2 = math.asin(n1/n2 * math.sin(theta1))         #formula to find the theta 
theta2 = math.degrees(theta2)                        #Changes value back to degrees 

#Writes the computed value as an output
stdio.writeln(theta2)
