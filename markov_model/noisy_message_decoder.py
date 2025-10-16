from markov_model import MarkovModel
import stdio
import sys

# Entry point.
def main():
    k = int(sys.argv[1])                  #Read order of K of Markov Model from command-line argument
    corrupted = sys.argv[2]               #Read corrupted string from command-line argument

    text = sys.stdin.read()               #Read original text from standard input

    model = MarkovModel(text, k)         

    decoded = model.replace_unknown(corrupted)

    stdio.writeln(decoded)

if __name__ == "__main__":
    main()
