import math
import stdio

# An immutable data type to represent a point in 3D space.
class Point3D:
    # Constructs a Point3D object given its x, y, and z coordinates.
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    # Returns the distance of this point to other.
    def distTo(self, other):
        x2 = self._x
        x1 = other._x
        y2 = self._y
        y1 = other._y
        z2 = self._z
        z1 = other._z
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    # Returns the distance of this point to the origin.
    def __abs__(self):
        x2 = self._x
        x1 = 0
        y2 = self._y
        y1 = 0
        z2 = self._z
        z1 = 0
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) 

    # Returns a Point3D object whose x, y, and z coordinates are the negative of this point's x, y, and z coordinates.
    def __neg__(self):
        x = -self._x
        y = -self._y
        z = -self._y

        return Point3D(x, y, z)
    
    # Returns True if this point's distance to the origin is less than the other point's distance to the origin; and 
    # False otherwise.
    def __lt__(self, other):
        return self.__abs__() < other.__abs__()

    # Returns True if this point and other have the same distance to the origin; and False otherwise.
    def __eq__(self, other):
        return self.__abs__() == other.__abs__()

    # Returns a string representation of this point.
    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ", " + str(self._z) + ")" 

# Unit tests the data type.
def _main():
    p1 = Point3D(1, 0)
    p2 = Point3D(0, 1)
    stdio.writeln(p1)
    stdio.writeln(p2)
    stdio.writeln(p1.distTo(p2))
    stdio.writeln(-p1)
    stdio.writeln(p1 < p2)
    stdio.writeln(p1 == p2)

if __name__ == "__main__":
    _main()
