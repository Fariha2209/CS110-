#imports all the necessary libraries
import stdio
import sys
import math

n = int(sys.argv[1])        #assigns n the command-line argument integer value

result = 1                  #sets result as 1
for i in range(1, n + 1):
   result = result * i      #updates the result value to a new value

stdio.writeln(result)       #writes the value of result