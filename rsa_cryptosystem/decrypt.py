import stdio
import sys
import rsa

n = int(sys.argv[1])
d = int(sys.argv[2])

width = len(bin(n)) - 2

message = stdio.readAll().strip()

binary_values = message.split()

for i in range(0, len(message) - 1, width):
    s = message[i: i + width]
    y = rsa.bin2dec(s)
    x = rsa.decrypt(y, n, d)

    stdio.write(chr(x))


     