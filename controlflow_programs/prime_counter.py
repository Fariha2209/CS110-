#imports necessary libraries 
import stdio
import sys

n = int(sys.argv[1])            #assigns n the command-line argument integer value

count = 0                       #sets count initial value to 0

for i in range(2, n + 1):      
    j = 2

    while j * j <= i:
        if i % j == 0:
            break
        j += 1

    if j * j > i:
        count += 1

stdio.writeln(count)          #writes the final value of count

