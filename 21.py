def fah_to_celsius(fahrenheit):
    return int((5/9)*(fahrenheit-32))

def celsius_to_fah(celsius):
    return ((9/5)*celsius+32)
ctof = []
ftoc = []
flag = True
while(flag):
    print("Enter choice:")
    print("1- Convert Fahrenheit to Celsius")
    print("2- Convert Celsius to Fahrenheit")
    print("3- Terminate the program")
    ch = int(input())
    if ch==1:
        print("Enter the temperature in Fahrenheit")
        t = float(input())
        res = fah_to_celsius(t)
        ftoc.append((t, res))
        print(res)
    elif ch==2:
        print("Enter the temperature in Celsius")
        t = float(input())
        res = celsius_to_fah(t)
        ctof.append((t, res))
        print(res)
    elif ch==3:
        flag = False
        ftoc = sorted(ftoc, key= lambda Y: Y[0])
        ctof = sorted(ctof, key= lambda Y: Y[0])
    else:
        print("You can't even get a choice right. What are you doing with your life ?")
        print("Try again, Piece of Shit!")
        print("\n")
print("\n")
print("List for Celsius to Fahrenheit Conversions")
print(ctof)
print("List for Fahrenheit to Celsius Conversions")
print(ftoc)
print("Exiting.......Satisfied?")