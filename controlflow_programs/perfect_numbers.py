#imports all the necessary libraries
import stdio
import sys

n = int(sys.argv[1])                     #assigns n the command-line argument integer value

for i in range(2 , n + 1):               #sets the range of 2 to n+1
    total = 0                            #sets total to 0

    for j in range(1, i //2 + 1):         #sets the range for j
        if i % j == 0:                    
            total += j                    #updates the value of total to the new value
    
    if total == i:
        stdio.writeln(i)


