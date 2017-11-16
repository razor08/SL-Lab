def list_max_finder(l):
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], list_max_finder(l[1:]))

print("Enter the list of numbers")
x = [int(x) for x in input().split()]
print(list_max_finder(x)) 