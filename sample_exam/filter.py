
import stdio
import sys
import math
from circle import Circle

def main():
    h = sys.argv[1]
    k = sys.argv[2]
    r = sys.argv[3]

    c = Circle(h, k, r)

    while not stdio.isEmpty():

        x = stdio.readFloat()
        y = stdio.readFloat()

        total += 1

        if c.contains(x, y):
            inside += 1

    stdio.writeln(inside / total)

if __name__ == "__main__":
    main()

