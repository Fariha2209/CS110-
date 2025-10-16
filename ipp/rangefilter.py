# Receives lo (int) and hi (int) as command-line inputs and integers as standard input; and writes as standard 
# output those integers that are in the range [lo, hi].

import stdio
import sys

lo = int(sys.argv[1])
hi = int(sys.argv[2])
while not stdio.isEmpty():
    x = stdio.readInt()
    if x >= lo and x <= hi:
        stdio.write(str(x) + " ")
stdio.writeln()
