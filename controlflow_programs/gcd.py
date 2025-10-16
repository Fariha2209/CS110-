#imports all the necessary libraries
import stdio
import sys
import math
import stdrandom

p = int(sys.argv[1])                 #assigns p the command-line argument value as an integer
q = int(sys.argv[2])                 #assigns q the command-line argument value as an integer

while p%q != 0:                      #sets a condition 
    t = p                            #assigns a temp value 
    p = q
    q = t % q
 
stdio.writeln(q)                     #writes the final value of q 