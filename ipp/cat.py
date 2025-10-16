# Receives sys.argv[1:n-2] files or web pages as command-line inputs; and copies them to the file whose name is 
# received as command-line input sys.argv[n-1].

from instream import InStream
from outstream import OutStream
import sys

# Entry point.
def main():
    n = len(sys.argv)
    outStream = OutStream(sys.argv[n - 1])
    for i in range(1, n - 1):
        inStream = InStream(sys.argv[i])
        s = inStream.readAll()
        outStream.write(s)

if __name__ == "__main__":
    main()
