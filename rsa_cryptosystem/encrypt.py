import stdio
import sys
import rsa

n = int(sys.argv[1])
e = int(sys.argv[2])
width = rsa.bitLength(n)

message = stdio.readAll()

for c in message: 
    x = ord(c)
    y = rsa.encrypt(x, n, e)
    stdio.writeln(rsa.dec2bin(y, width))
stdio.writeln()