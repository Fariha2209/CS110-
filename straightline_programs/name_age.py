#writes the message "name is age years old"
#receives a name and age as a command-line argument


import stdio
import sys


name = sys.argv[1]  #imports first command-line argument as name   
age = sys.argv[2]   #imports second command-line rgument as age

stdio.write(name + " is " + age + " years old.") 



