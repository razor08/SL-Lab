def ctof(c):
    return c*9/5+32
def ftoc(f):
    return (f-32)*5/9

cf = []
fc = []
f1 = True
while(f1):
    ch = int(input("Choice: 1-Celsius to Fahrenheit\n2-Fahrenheit to Celsius\n3-View\n4-Exit"))
    if ch==4:
        f1 = False
    elif ch==1 or ch==2:
        t = float(input("Enter the temperature to be converted"))
        if ch==1:
            tn = ctof(t)
            print(t, "C -> ", tn, "F")
            cf.append((t, tn))

        if ch==2:
            tn = ftoc(t)
            print(t, "F -> ", tn, "C")
            fc.append((t, tn))
    elif ch==3:
        x = int(input("Choice: 1-Sort by Input\n2-Sort by output"))
        if x==1:
            print("Input Order")
            print(sorted(fc, key=lambda x:x[0]))
            print(sorted(cf, key=lambda x:x[0]))
        else:
            print("Output Order")
            print(sorted(fc, key=lambda x:x[1]))
            print(sorted(cf, key=lambda x:x[1]))
    else:
        print("Wrong Choice. Please try again!")
