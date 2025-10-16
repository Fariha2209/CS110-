"""
The picture library defines the Picture class.
"""

import color
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame


class Picture:
    """
    A Picture object models an image.
    """

    def __init__(self, arg1=None, arg2=None):
        """
        If both arg1 and arg2 are None, then construct self such that it is all black with width
        512 and height 512. If arg1 is not None and arg2 is None, then construct self by reading
        from the file whose name is arg1. If neither arg1 nor arg2 is None, then construct self
        such that it is all black with width arg1 and height arg2.
        """
        if (arg1 is None) and (arg2 is None):
            maxW = 512
            maxH = 512
            self._surface = pygame.Surface((maxW, maxH))
            self._surface.fill((0, 0, 0))
        elif (arg1 is not None) and (arg2 is None):
            fileName = arg1
            try:
                self._surface = pygame.image.load(fileName)
            except pygame.error:
                raise IOError()
        elif (arg1 is not None) and (arg2 is not None):
            maxW = arg1
            maxH = arg2
            self._surface = pygame.Surface((maxW, maxH))
            self._surface.fill((0, 0, 0))
        else:
            raise ValueError()

    def save(self, f):
        """
        Save self to the file whose name is f.
        """
        pygame.image.save(self._surface, f)

    def width(self):
        """
        Return the width of self.
        """
        return self._surface.get_width()

    def height(self):
        """
        Return the height of self.
        """
        return self._surface.get_height()

    def get(self, x, y):
        """
        Return the color of self at location (x, y).
        """
        pygameColor = self._surface.get_at((x, y))
        return color.Color(pygameColor.r, pygameColor.g, pygameColor.b)

    def set(self, x, y, c):
        """
        Set the color of self at location (x, y) to c.
        """
        pygameColor = pygame.Color(c.getRed(), c.getGreen(), c.getBlue(), 0)
        self._surface.set_at((x, y), pygameColor)


# Unit tests the library.
def _main():
    import sys

    inFileName = sys.argv[1]
    outFileName = sys.argv[2]
    picture1 = Picture(inFileName)
    picture2 = Picture(picture1.width(), picture1.height())
    for col in range(picture2.width()):
        for row in range(picture2.height()):
            pixel = picture1.get(col, row)
            picture2.set(col, row, pixel.toGray())
    picture2.save(outFileName)


if __name__ == "__main__":
    _main()
