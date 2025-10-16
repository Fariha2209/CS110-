#imports necessary libraries
import stdio
import sys

#Takes the command-line inputs and assigns them to the designated variables
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])


q = 1 - p   #calculates the complementary probability using the formula
p1 = (1 - (p/q)**n2)/(1 - (p/q)**(n1 + n2))   #formula to calculate p1
p2 = (1 - (q/p)**n1)/(1 - (q/p)**(n1 + n2))   #formula to calculate p2

stdio.writeln(str(p1) + " " + str(p2))        #generates an output with p1 and p2 with space inbetween
