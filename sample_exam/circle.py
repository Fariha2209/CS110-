
import sys
import math

class Circle:

    def __init__(self, h = 0, k = 0, r = 1):
        self._h = h
        self._k = k
        self._r = r
    
    def area(self):
        return math.pi * self._r ** 2
    
    def circumference(self):
        return 2 * math.pi * self._r 
    
    def contains(self, x, y):
        return (self._h - x) ** 2 + (self._k - y) ** 2 <= self._r ** 2
    
    def scale(self, r):
        return Circle(self._h, self._k, r)
    
    def distanceTo(self, other):
        return ((self._h - other._h) ** 2 + (self._k - other._k) ** 2) ** 0.5
    
    def __eq__(self, other):
        return self._h == other._h and self._k == other._k and self._r == other._r
    
    def __lt__(self, other):
        return self.area() < other.area()

    def __str__(self):
        return "(" + str(self._h) + ", " +  str(self._k) + ", " + str(self._r) + ")"

def main():
    import stdio