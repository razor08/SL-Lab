class SentenceReverser:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sentence = ""
    reverse = ""
    vowelCount = 0
    def __init__(self, sentence):
        self.sentence = sentence
        self.reverseSentence()
    def reverseSentence(self):
        self.reverse = " ".join(reversed(self.sentence.split()))
    def getVowelCount(self):
        wordList = self.sentence.split(" ")
        res = 0
        for x in range(len(wordList)):
            for y in range(len(wordList[x])):
                if wordList[x][y] in self.vowels:
                    res = res + 1
        self.vowelCount = res
        return self.vowelCount
    def getReverse(self):
        return self.reverse

items = []

for x in range(3):
    print("Enter phrase number: " + str(x+1))
    sentence = str(input())
    reverser = SentenceReverser(sentence)
    items.append(reverser)

sortedItems = sorted(items, key=lambda item: item.getVowelCount(), reverse = True)

for x in range(len(sortedItems)):
    print("Reverse: " + sortedItems[x].getReverse() + " Vowel Count: " + str(sortedItems[x].getVowelCount()))