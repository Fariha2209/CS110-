#imports all the necessary libraries
import stdio
import sys

n = int(sys.argv[1])            #assigns n the command-line argument value as an integer

a = -1                          #assigns "a" a value
b = 1                           #assigns b a value
i = 0                           #asigns i the value 0

while i <= n:                   #sets the condition that the loop runs until i <= n
    temp = a + b                 
    a = b
    b = temp                    #sets a temp value to reassign values
    i = i + 1                   #updates the value of i after every iteration

stdio.writeln(b)                #writes the final value of b

    
