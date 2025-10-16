# Receives n (int) as a command-line input; and writes as standard output the number of coupons one must collect 
# before obtaining one of each of the n types.

import stdarray
import stdio
import stdrandom
import sys

n = int(sys.argv[1])
count = 0
collectedCount = 0
isCollected = stdarray.create1D(n, False)
while collectedCount < n:
    value = stdrandom.uniformInt(0, n)
    count += 1
    if not isCollected[value]:
        collectedCount += 1
        isCollected[value] = True
stdio.writeln(count)
