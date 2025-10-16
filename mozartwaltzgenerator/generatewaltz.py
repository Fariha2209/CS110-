#importing necessary libraries
import stdio
import sys
import stdarray
import stdrandom

minuetMeasures = stdarray.create2D(11, 16, 0)         #Creates a 2D list

#Start with a  for loop (nested loop)

for i in range (11):                                 #starts a for loop    
    for j in range(16):
        minuetMeasures[i][j] = stdio.readInt()
        #d1 = stdrandom.uniformInt(1, 7)
        #d2 = stdrandom.uniformInt(1, 7)
        #i = d1 + d2 - 2
        #stdio.writeln(str(minuetMeasures[i][j]) + " ")           
        #minuetMeasures[i][j] = stdio.readInt()        #assigns a value to the 2D list based on row and column from the dataset

trioMeasures = stdarray.create2D(6, 16, 0)

for i in range(6):
    for j in range(16):
        trioMeasures[i][j] = stdio.readInt()

for j in range(16):
    d1 = stdrandom.uniformInt(1, 7)
    d2 = stdrandom.uniformInt(1, 7)
    i = d1 + d2 - 2
    stdio.writeln(str(minuetMeasures[i][j]) + " ")

for j in range(16):
    d1 = stdrandom.uniformInt(1, 7)
    i = d1 - 1
    stdio.writeln(str(trioMeasures[i][j]) + " ")

stdio.writeln()                   
    



