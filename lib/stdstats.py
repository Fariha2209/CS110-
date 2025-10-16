"""
The stdstats library defines functions related to statistical analysis and graphical data display.
"""

import math
import stddraw


def mean(a):
    """
    Return the average of the elements of array a.
    """
    return sum(a) / float(len(a))


def var(a):
    """
    Return the sample variance of the elements of array a.
    """
    mu = mean(a)
    total = 0.0
    for x in a:
        total += (x - mu) * (x - mu)
    return total / (float(len(a)) - 1.0)


def stddev(a):
    """
    Return the standard deviation of the elements of array a.
    """
    return math.sqrt(var(a))


def median(a):
    """
    Return the median of the elements of array a.
    """
    b = a[:]  # Make a copy of a.
    b.sort()
    n = len(b)
    if n % 2 == 1:
        return b[n // 2]
    else:
        return float(b[n // 2 - 1] + b[n // 2]) / 2.0


def plotPoints(a):
    """
    Plot the elements of array a as points.
    """
    n = len(a)
    stddraw.setXscale(-1, n)
    stddraw.setPenRadius(1.0 / (3.0 * n))
    for i in range(n):
        stddraw.point(i, a[i])


def plotLines(a):
    """
    Plot the elements of array a as line end-points.
    """
    n = len(a)
    stddraw.setXscale(-1, n)
    stddraw.setPenRadius(0.0)
    for i in range(1, n):
        stddraw.line(i - 1, a[i - 1], i, a[i])


def plotBars(a):
    """
    Plot the elements of array a as bars.
    """
    n = len(a)
    stddraw.setXscale(-1, n)
    for i in range(n):
        stddraw.filledRectangle(i - 0.25, 0.0, 0.5, a[i])


# Unit tests the library.
def _main():
    import stdio
    import stdrandom
    import sys

    testID = sys.argv[1]
    a = []
    for i in range(15):
        a.append(round(stdrandom.uniformFloat(0, 1), 3))
    if testID == "stats":
        stdio.writeln("a         = " + str(a))
        stdio.writeln("mean(a)   = " + str(round(mean(a), 3)))
        stdio.writeln("var(a)    = " + str(round(var(a), 3)))
        stdio.writeln("stddev(a) = " + str(round(stddev(a), 3)))
        stdio.writeln("median(a) = " + str(median(a)))
    elif testID == "plotPoints":
        plotPoints(a)
        stddraw.show()
    elif testID == "plotLines":
        plotLines(a)
        stddraw.show()
    elif testID == "plotBars":
        plotBars(a)
        stddraw.show()


if __name__ == "__main__":
    _main()
