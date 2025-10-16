# Receives x (int) and y (int) as command-line inputs; and writes the sum of their squares as standard output.

import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
result = x * x + y * y
stdio.writeln(result)
