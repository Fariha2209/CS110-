#imports necessary libraries
import stdio
import sys

n = int(sys.argv[1])         #assigns n the command-line argument integer value 

a = 1                        #sets a the value 1 

while a**3 <= n:             #starts a loop to go through the values of a until a**3 is less than or equal to 0        
    b = (a + 1)              #sets b the value a + 1

    while a**3 + b**3 <= n:      #starts another loop 
        c = a + 1                #sets c the value a + 1

        while c**3 <= n:         #starts another loop
            d = c + 1            #sets d the value c + 1

            while c**3 + d**3 <= n:         #starts another loop 
                x = a**3 + b**3             #sets x value
                y = c**3 + d**3             #sets y value
                if x == y:
                    stdio.writeln(str(x) + " = " + str(a) + "^3 + "  + str(b) + "^3 = " + str(c) + "^3 +" + str(d) + "^3")
                    
                d += 1        #increments by 1 
            c += 1
        b += 1
    a += 1




