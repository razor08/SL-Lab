def list_max(l):
    if len(l) == 1:
        return l[0]
    else:
        m = list_max(l[1:])
        return m if m>l[0] else l[0]



l = [int(x) for x in input().split()]

print(list_max(l))