import sys
import os
import functools
if (len(sys.argv)!=2):
    print("Invalid arguments")
    sys.exit()
if (not(os.path.exists(sys.argv[1]))):
    print("File given not present")
    sys.exit()
if (sys.argv[1].split(".")[-1] != "txt"):
    print("Only txt files allowed!")
    sys.exit()

esc = open(sys.argv[1])

worddic = {}
for line in esc:
    myline = line.split()
    for word in myline:
        w = worddic.get(word, 0)
        worddic[word] = w + 1 
print(worddic, "\n")

sortedlist = sorted(worddic.items(), reverse = True)

sortedlist = sorted(worddic.items(), key = lambda Y: Y[1], reverse = True)

top_ten = []
for i in range(10):
    wordTuple = sortedlist[i]
    print(wordTuple)
    top_ten.append(len(wordTuple[0]))
    print("\n", wordTuple[0], " frequency: ", wordTuple[1], " length: ", top_ten[i])

print("Length of top ten occuring words")
print(top_ten)

mysum = functools.reduce(lambda x, y: x+y, top_ten)
print("Average length of top ten most occuring words: " + str(mysum//10))

print([x**2 for x in top_ten if top_ten[x]%2==0])