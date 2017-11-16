def fah_to_celsius(fahrenheit):
    return (5/9)*(fahrenheit-32)

def celsius_to_fah(celsius):
    return ((9/5)*celsius+32)
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
        print(fah_to_celsius(t))
    elif ch==2:
        print("Enter the temperature in Celsius")
        t = float(input())
        print(celsius_to_fah(t))
    elif ch==3:
        flag = False
    else:
        print("You can't even get a choice right. What are you doing with your life ?")
        print("Try again, Piece of Shit!")
        print("\n")
print("\n")
print("Exiting.......Satisfied?")