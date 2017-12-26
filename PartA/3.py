from collections import Counter

fname = "sample.txt"
def word_counter(fname):
    with open(fname) as f:
        return Counter(f.read().split())
print("Occurence of each word in " + fname + " is: " , word_counter(fname) , "\n")