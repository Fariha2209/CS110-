#imports all the necessary libraries
import stdio
import sys
import math

n = int(sys.argv[1])          #assigns n the command-line argument integer value


i = 2                         #sets i to 2
while i <= n / i:             #starts the while loop that checks for condition of primality
  if n % i == 0:
    stdio.writeln(False)
    break
  i += 1                 #updates value of i to the new value aftr every iteration

if i > n / i:  
   stdio.writeln(True)        

