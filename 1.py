def detect_duplicate(l):
    li = []
    for x in range(len(l)):
        if l[x] not in li:
            li.append(l[x])

    return li
print("Enter the list to be checked for duplicates")
l = [int(x) for x in input().split()]
li = detect_duplicate(l)
print("List with no duplicates")
print(li)

