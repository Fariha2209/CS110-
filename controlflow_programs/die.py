#imports all necessary libraries
import stdio
import sys
import math
import stdrandom

value = stdrandom.uniformInt(1, 7)               #generates a random value within the range 1 - 7

#Assigns each generated value to an output message
if value == 1:
    stdio.writeln("  *  \n     \n     ")
elif value == 2:
    stdio.writeln("*    \n     \n    *")
elif value == 3:
    stdio.writeln("*    \n  *  \n    *")
elif value == 4:
    stdio.writeln("*   *\n     \n*   *")
elif value == 5:
    stdio.writeln("*   *\n  *  \n*   *")
elif value == 6:
    stdio.writeln("* * *\n     \n* * *")

