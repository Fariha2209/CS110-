import stdio
import sys
import rsa


def main():

    if len(sys.argv) != 3:
        stdio.writeln("Usage: python3 keygen.py <lo> <hi>")
        sys.exit(1)
        

    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    keys = rsa.keygen(lo, hi)

    stdio.writef("%d %d %d\n", keys[0], keys[1], keys[2])

if __name__ == "__main__":
    main()

# def main():
#     if len(sys.argv) != 3:
#         stdio.writeln("Usage: python3 keygen.py <lo> <hi>")
#         sys.exit(1)

#     lo = int(sys.argv[1])
#     hi = int(sys.argv[2])

#     n, e, d = keygen(lo, hi)

#     stdio.writeln( str(n) + " " + str(e) + " " + str(d))

# if __name__ == "__main__":
#     main()