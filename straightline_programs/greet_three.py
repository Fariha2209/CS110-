#writes a message "Hi name3, name2, and name1."

import stdio
import sys

#receives name1, name2, and name3 as command-line argument
name1 = sys.argv[1]
name2 = sys.argv[2]
name3 = sys.argv[3]

stdio.write("Hi " + name3 + ", " + name2 + "," + " and " + name1 + ".") 

