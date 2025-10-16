
import stdio
import sys
import math


r = float(sys.argv[1])
theta = float(sys.argv[2])
theta = math.radians(theta)

x = r * math.cos(theta)
y = r * math.sin(theta)

stdio.writeln(str(x) + " " + str(y))
