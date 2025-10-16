import stdio
import math


# A data type to represent a blob.
class Blob:
    # Constructs an empty blob.
    def __init__(self):
        self._x = 0
        self._y = 0
        self._pixels = 0

    # Adds pixel (x, y) to this blob.
    def add(self, x, y):
        self._x = (self._x * self._pixels + x )/(self._pixels + 1)
        self._y = (self._y * self._pixels + y )/(self._pixels + 1)
        self._pixels += 1

    # Returns the mass of this blob, ie, the number of pixels in it.
    def mass(self):
        return self._pixels

    # Returns the Euclidean distance between the center of mass of this blob and the center of
    # mass of the other blob.
    def distanceTo(self, other):
        
        x1 = self._x
        x2 = other._x
        y1 = self._y
        y2 = other._y
        distance = math.sqrt(( x1 - x2) ** 2 + ( y1 - y2) ** 2)

        return distance

    # Returns a string representation of this blob.
    def __str__(self):
        return "%d (%.4f, %.4f)" % (self._pixels, self._x, self._y)


# Unit tests the data type [DO NOT EDIT].
def _main():
    a = Blob()
    a.add(0, 0)
    b = Blob()
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        b.add(x, y)
    stdio.writeln("a          = " + str(a))
    stdio.writeln("b          = " + str(b))
    stdio.writeln("dist(a, b) = " + str(a.distanceTo(b)))


if __name__ == "__main__":
    _main()
