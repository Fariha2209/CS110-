#Importing necessary libraries
import stdio
import sys
import math
import stdrandom

n = int(sys.argv[1])                                #Reads the command-line input argument
die_1 = stdrandom.uniformInt(1, n + 1)              #Generates a random number between the range 1 and n + 1 for the first die roll 
die_2 = stdrandom.uniformInt(1, n + 1)              #Generates a random number between the range 1 and n + 1 for the second die roll

sum = (die_1 + die_2)                               #Creates a formula for the sum of the random numbers from the die rolls

#Writes the computed result 
stdio.writeln(sum)                             


