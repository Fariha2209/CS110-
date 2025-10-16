
#imports all the necessary libraries
import stdio
import sys

#Reads the command-line inputs
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])
G = 6.674 * (10 ** -11)     #Defines the value of G

f = (G * m1 * m2) / (r ** 2)       #Formula used to calculate 

#Generates the calculated result 
stdio.writeln(f)




