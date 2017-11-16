print("Upto what range do you want even numbers to be printed out ?")

n = int(input())
S = [int(x) for x in range(1, n+1)]


M = [int(z) for z in S if z%2==0 ]
print(M)

print("Printing in Reverse Order")
M.reverse()
print(M)