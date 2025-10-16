"""
The color library defines the Color data type.
"""


class Color:
    """
    The Color data type models an RGB color.
    """

    def __init__(self, r=0, g=0, b=0):
        """
        Construct self such that it has the given red (r), green (g), and blue (b) components.
        """
        self._r = r  # Red component
        self._g = g  # Green component
        self._b = b  # Blue component

    def getRed(self):
        """
        Return the red component of self.
        """
        return self._r

    def getGreen(self):
        """
        Return the green component of self.
        """
        return self._g

    def getBlue(self):
        """
        Return the blue component of self.
        """
        return self._b

    def luminance(self):
        """
        Return the luminance of self.
        """
        return 0.299 * self.getRed() + 0.587 * self.getGreen() + 0.114 * self.getBlue()

    def toGray(self):
        """
        Return the grayscale equivalent of self.
        """
        y = int(round(self.luminance()))
        return Color(y, y, y)

    def isCompatible(self, other):
        """
        Return True if self is compatible with other, and False otherwise.
        """
        return abs(self.luminance() - other.luminance()) >= 128

    def __str__(self):
        """
        Return the string representation of self.
        """
        return ("(" + str(self.getRed()) + ", " + str(self.getGreen()) + ", "
                + str(self.getBlue()) + ")")


# Unit tests the library.
def _main():
    import stdio
    import sys

    r = int(sys.argv[1])
    g = int(sys.argv[2])
    b = int(sys.argv[3])
    c1 = Color(r, g, b)
    c2 = Color(64, 64, 64)
    stdio.writeln("c1                  = " + str(c1))
    stdio.writeln("c2                  = " + str(c2))
    stdio.writeln("c1.luminance()      = " + str(c1.luminance()))
    stdio.writeln("c1.toGray()         = " + str(c1.toGray()))
    stdio.writeln("c1.isCompatible(c2) = " + str(c1.isCompatible(c2)))


if __name__ == "__main__":
    _main()
