#importing all necessary values
import stdio
import sys
import math

n = int(sys.argv[1])        #takes the command-line argument as integer input

dragon = "F"                #gives variable dragon a value
nogard = "F"                #gives variable nogard a value

for i in range(1, n + 1):              #starts a for loop that iterates the range 1, n + 1
    temp = dragon                      #assigns temp the value dragon
    dragon = dragon + "L" + nogard           
    nogard = temp + "R" + nogard
 
stdio.writeln(dragon)                   #writes the result