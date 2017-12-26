import os, functools, sys

esc = open(sys.argv[1])

word_dic = {}

for line in esc:
    my_line = line.split()
    for word in my_line:
        w = word_dic.get(word, 0)
        word_dic[word] = w + 1

print(word_dic)

sorted_list = sorted(word_dic.items(), key = lambda x:x[1], reverse = True )
print('Sorted list by occurences:')
print(sorted_list)

top_ten = []
for i in range(10):
    word_tuple = sorted_list[i]
    top_ten.append(len(word_tuple[0]))
    print(word_tuple[0], " Frequency: ", word_tuple[1], " Length: ", len(word_tuple[0]))
print("Length of top ten occurring words.")
print(top_ten)

mysum = functools.reduce(lambda x,y:x+y, top_ten)

print(mysum/10)

squares =[x**2 for x in top_ten if x%2!=0]

print("Squares: ", squares)


