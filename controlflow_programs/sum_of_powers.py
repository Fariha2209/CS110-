#imports all the necessary values
import stdio
import sys
import math

n = int(sys.argv[1])      #sets the value of n as the command-line argument as an int
k = int(sys.argv[2])      #sets the value of k as the command-line argument as an int

total = 0                 #sets total to 0

for i in range(1, n + 1):       #starts a for loop 
    total += i ** k             #updates the total value

stdio.writeln(total)            #writes the final results
