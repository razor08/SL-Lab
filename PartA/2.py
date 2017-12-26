def list_reader(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
        else:
            pass
    return x

l = [int(x) for x in input().split()]
print(list_reader(l))