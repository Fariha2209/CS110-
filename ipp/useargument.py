# Receives a name as command-line input; and writes a message containing that name as standard output.

import stdio
import sys

stdio.write("Hi, ")
stdio.write(sys.argv[1])
stdio.writeln(". How are you?")
