from symboltable import SymbolTable
import stdio
import stdrandom

class MarkovModel(object):
    # Creates a Markov model of order k from the given text.
    def __init__(self, text, k):

        self._k = k                                    #length of kgrams
        self._st = SymbolTable()                       #symbol table to store kgrams and their char frequencies
        self._text = text + text[:k]                   

        for i in range(len(text)):                     #Loop through each kgram and store their frequency of next char
            kgram = self._text[i:i + k]
            next_char = self._text[i + k]

            if kgram not in self._st:
                self._st[kgram] = SymbolTable()

            freq_table = self._st[kgram]               #Frequency table for chars following this kgram

            #Increment frequency count for next char
            if next_char in freq_table:
                freq_table[next_char] += 1
            else:
                freq_table[next_char] = 1
   

    # Returns the order this Markov model.
    def order(self):
        return self._k

    # Returns the number of occurrences of kgram in this Markov model; and 0 if kgram is nonexistent. Raises an error 
    # if kgram is not of length k.
    def kgram_freq(self, kgram):
        if len(kgram) != self._k:
            raise ValueError("kgram must be of length k")
        elif kgram not in self._st:
            return 0           #kgram does not exist
        
        total = 0
        freq_table = self._st[kgram]
        #sum frequencies of all characters
        for key in freq_table.keys():
            total += freq_table[key]
        return total

    # Returns number of times character c follows kgram in this Markov model; and 0 if kgram is nonexistent or if it 
    # is not followed by c. Raises an error if kgram is not of length k.
    def char_freq(self, kgram, c):
        if len(kgram) != self._k:
            raise ValueError("kgram must be of length k")
        elif kgram not in self._st or c not in self._st[kgram]:
            return 0
        
        freq_table = self._st[kgram]
        if c in freq_table:
            return freq_table[c]
        else:
            return 0

        
    # Returns a random character following kgram in this Markov model. Raises an error if kgram is not of length k or 
    # if kgram is nonexistent.
    def rand(self, kgram):
        if len(kgram) != self._k:
            raise ValueError("kgram must be of length k")
        if kgram not in self._st:
            raise ValueError("kgram does not exist")
        
        freq_table = self._st[kgram]
        
        chars = []
        freqs = []

        #extracts chars and their frquencies
        for key in freq_table.keys():
            chars.append(key)
            freqs.append(freq_table[key])

        index = stdrandom.discrete(freqs)             #Choose an index randomly based on frequency

        return chars[index]

    # Generates and returns a string of length n from this Markov model, the first k characters of which is kgram.
    def gen(self, kgram, n):
        
        text = kgram

        #generate each next character based on previous k chars
        for i in range( n - self._k):
            next_char = self.rand(text[i: self._k + i])
            text += next_char

        return text

    # Replaces unknown characters (~) in corrupted with most probable characters from this Markov model, and returns 
    # that string.
    def replace_unknown(self, corrupted):
        original = ""
        for i in range(len(corrupted)):
            if corrupted[i] == "~":

                kgram_before = corrupted[i - self._k : i]
                kgram_after = corrupted[i + 1:i + 1 + self._k]

                probs = []                                 #store probability for each hypothesis character
                hypotheses = []                            #possible characters that could replace '~'

                for h in self._st[kgram_before].keys():
                    hypotheses.append(h)
                    context = kgram_before + h + kgram_after
                    p = 1.0
                    
                    for c in range(self._k):
                        kgram = context[c: c + self._k]
                        char = context[c + self._k]

                        if kgram not in self._st or char not in self._st[kgram]:
                            p = 0.0
                            break
                        prob = self._st[kgram][char] / self.kgram_freq(kgram)
                        p *= prob

                    probs.append(p)
                #Find the hypothesis with the highest probability
                best_index = _argmax(probs)
                best_char = hypotheses[best_index]
                original += best_char
            else:
                original += corrupted[i]

        return original

# Given a list a, _argmax returns the index of the maximum value in a.
def _argmax(a):
    return a.index(max(a))

# Unit tests the data type [DO NOT EDIT].
def _main():
    model = MarkovModel("gagggagaggcgagaaa", 2)
    stdio.writeln("model       = MarkoveModel(\"gagggagaggcgagaaa\", k = 2)")
    stdio.writef("freq(ag)    = %d\n", model.kgram_freq("ag"))
    stdio.writef("freq(cg)    = %d\n", model.kgram_freq("cg"))
    stdio.writef("freq(gc)    = %d\n", model.kgram_freq("gc"))
    stdio.writef("freq(xx)    = %d\n", model.kgram_freq("xx"))
    stdio.writef("freq(aa, a) = %d\n", model.char_freq("aa", "a"))
    stdio.writef("freq(ga, g) = %d\n", model.char_freq("ga", "g"))
    stdio.writef("freq(gg, c) = %d\n", model.char_freq("gg", "c"))
    stdio.writef("freq(xx, x) = %d\n", model.char_freq("xx", "x"))
    stdio.writef("freq(gg, x) = %d\n", model.char_freq("gg", "x"))

if __name__ == "__main__":
    _main()
