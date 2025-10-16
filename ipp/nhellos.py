# Receives n (int) as command-line input; and writes n Hellos as standard output.

import stdio
import sys

n = int(sys.argv[1])
i = 1
while i <= n:
    stdio.writeln("Hello # " + str(i))
    i += 1
