class SentenceReverser():
    sent = ""
    rev_sent =""
    vowel_list = ['a' ,'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_count = 0
    def __init__(self, sent):
        self.sent = sent
        self.sent_reverse()

    def sent_reverse(self):
        l = self.sent.split()
        self.rev_sent =  ' '.join(reversed(l))

    def get_vowel_count(self):
        word_list = self.sent.split()
        res = 0
        for x in word_list:
            for y in range(len(x)):
                if x[y] in self.vowel_list:
                    res = res + 1
        self.vowel_count = res
        return res

    def get_reverse(self):
        return self.rev_sent

items = []
for x in range(3):
    s = input("Enter sentence " + str(x+1) + "\n")
    sent = SentenceReverser(s)
    items.append(sent)

sorted_items = sorted(items,key= lambda item:item.get_vowel_count(), reverse = True)

for x in range(len(sorted_items)):
    print("Reverse: " + sorted_items[x].get_reverse() + " Vowel Count: " + str(sorted_items[x].get_vowel_count()))