# Receives a sequence of strings as standard input; and writes the strings in reverse order as standard output.

from stack import Stack
import stdio

# Entry point.
def main():
    stack = Stack()
    while not stdio.isEmpty():
        stack.push(stdio.readString())
    for s in stack:
        stdio.write(s + " ")
    stdio.writeln()

if __name__ == "__main__":
    main()
