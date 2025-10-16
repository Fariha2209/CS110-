"""
The outstream library defines the OutStream class.
"""

import sys


class OutStream:
    """
    An OutStream object wraps around a text file or sys.stdout, and supports writing to that stream.
    """

    def __init__(self, f=None):
        """
        Construct self to wrap around a stream. If f is provided, then the stream is a file of
        that name. Otherwise, the stream is standard output.
        """
        if f is None:
            self._stream = sys.stdout
        else:
            if sys.hexversion < 0x03000000:
                self._stream = open(f, "w")
            else:
                self._stream = open(f, "w", encoding="utf-8")

    def writeln(self, x=""):
        """
        Write x and an end-of-line mark to the stream wrapped by self.
        """
        if sys.hexversion < 0x03000000:
            x = x.encode("utf-8")
        else:
            x = str(x)
        self._stream.write(x)
        self._stream.write("\n")
        self._stream.flush()

    def write(self, x=""):
        """
        Write x to the stream wrapped by self.
        """
        if (sys.hexversion < 0x03000000):
            x = x.encode("utf-8")
        else:
            x = str(x)
        self._stream.write(x)
        self._stream.flush()

    def writef(self, fmt, *args):
        """
        Write each element of args to the stream wrapped by self. Use the format specified by
        string fmt.
        """
        x = fmt % args
        if sys.hexversion < 0x03000000:
            x = x.encode("utf-8")
        self._stream.write(x)
        self._stream.flush()

    def __del__(self):
        """
        Close the stream wrapped by self.
        """
        self._stream.close()


# Unit tests the library.
def _main():
    import math

    if len(sys.argv) > 1:
        outStream = OutStream(sys.argv[1])
    else:
        outStream = OutStream()
    outStream.write("Hello, World!")
    outStream.writeln()
    outStream.writef("The value of PI up to 15 decimal places is %.15f.\n", math.pi)


if __name__ == "__main__":
    _main()
