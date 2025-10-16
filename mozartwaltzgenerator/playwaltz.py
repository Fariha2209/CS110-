#importing necessary libraries
import stdio
import sys
import stdrandom
import stdarray
import stdaudio


#take inputs from generatwaltz.py
measure = stdio.readAllInts()

#checks if there are exactly 32 measures
if len(measure) != 32:
    sys.exit("A waltz must contain exactly 32 measures")

#validates the frist 16 values
for i in range(16):
    number = measure[i]
    if number < 1 or number > 176:
        sys.exit("A minuet measure must be from [1, 176]")

#validates the last 16 values
for i in range(16, 32):
    number = measure[i]
    if number < 1 or number > 96:
        sys.exit("A trio measure must be from [1, 96]")

#writes filename and plays minuet
for i in range(16):
    v = measure[i]
    filename = "data/M" + str(v)
    stdaudio.playFile(filename)

#writes filename and plays trio 
for i in range(16, 32):
    v = measure[i]
    filename = "data/T" + str(v)
    stdaudio.playFile(filename)


