"""
The stdarray library defines functions related to creating, reading, and writing one- and
two-dimensional lists.
"""

import stdio


def create1D(length, value=None):
    """
    Create and return a 1D list containing length elements, each initialized to value.
    """
    return [value] * length


def create2D(rowCount, colCount, value=None):
    """
    Create and return a 2D list having rowCount rows and colCount columns, with each element
    initialized to value.
    """
    a = create1D(rowCount)
    for row in range(rowCount):
        a[row] = create1D(colCount, value)
    return a


def readInt1D():
    """
    Read from sys.stdin and return a list of integers. An integer at the beginning of sys.stdin
    defines the list's length.
    """
    count = stdio.readInt()
    a = create1D(count)
    for i in range(count):
        a[i] = stdio.readInt()
    return a


def readInt2D():
    """
    Read from sys.stdin and return a two-dimensional list of integers. Two integers at the
    beginning of sys.stdin define the list's dimensions.
    """
    rowCount = stdio.readInt()
    colCount = stdio.readInt()
    a = create2D(rowCount, colCount)
    for row in range(rowCount):
        for col in range(colCount):
            a[row][col] = stdio.readInt()
    return a


def readFloat1D():
    """
    Read from sys.stdin and return a list of floats. An integer at the beginning of sys.stdin
    defines the list's length.
    """
    count = stdio.readInt()
    a = create1D(count)
    for i in range(count):
        a[i] = stdio.readFloat()
    return a


def readFloat2D():
    """
    Read from sys.stdin and return a two-dimensional list of floats. Two integers at the
    beginning of sys.stdin define the list's dimensions.
    """
    rowCount = stdio.readInt()
    colCount = stdio.readInt()
    a = create2D(rowCount, colCount)
    for row in range(rowCount):
        for col in range(colCount):
            a[row][col] = stdio.readFloat()
    return a


def readBool1D():
    """
    Read from sys.stdin and return a list of booleans. An integer at the beginning of sys.stdin
    defines the list's length.
    """
    count = stdio.readInt()
    a = create1D(count)
    for i in range(count):
        a[i] = stdio.readBool()
    return a


def readBool2D():
    """
    Read from sys.stdin and return a two-dimensional list of booleans. Two integers at the
    beginning of sys.stdin define the list's dimensions.
    """
    rowCount = stdio.readInt()
    colCount = stdio.readInt()
    a = create2D(rowCount, colCount)
    for row in range(rowCount):
        for col in range(colCount):
            a[row][col] = stdio.readBool()
    return a


def write1D(a):
    """
    Write list a to sys.stdout. First write its length. bool objects are written as 0 and 1,
    not False and True.
    """
    length = len(a)
    stdio.writeln(length)
    for i in range(length):
        element = a[i]
        if isinstance(element, bool):
            if element == True:
                stdio.write(1)
            else:
                stdio.write(0)
        else:
            stdio.write(element)
        stdio.write(" ")
    stdio.writeln()


def write2D(a):
    """
    Write two-dimensional list a to sys.stdout. First write its dimensions. bool objects are
    written as 0 and 1, not False and True.
    """
    rowCount = len(a)
    colCount = len(a[0])
    stdio.writeln(str(rowCount) + " " + str(colCount))
    for row in range(rowCount):
        for col in range(colCount):
            element = a[row][col]
            if isinstance(element, bool):
                if element == True:
                    stdio.write(1)
                else:
                    stdio.write(0)
            else:
                stdio.write(element)
            stdio.write(" ")
        stdio.writeln()


# Unit tests the library.
def _main():
    import sys

    testId = sys.argv[1]
    map = {
        "readInt1D": readInt1D, "readInt2D": readInt2D,
        "readFloat1D": readFloat1D, "readFloat2D": readFloat2D,
        "readBool1D": readBool1D, "readBool2D": readBool2D}
    if testId.endswith("1D"):
        write1D(map[testId]())
    elif testId.endswith("2D"):
        write2D(map[testId]())


if __name__ == "__main__":
    _main()
