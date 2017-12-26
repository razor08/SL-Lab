class Student:
    usn = ""
    name = ""
    m1 = 0
    m2 = 0
    m3 = 0

    def __init__(self, name, usn, m1, m2, m3):
        self.usn = usn
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate(self):
        print("Total for: " + self.usn + " is: "+ str(self.m1+self.m2+self.m3))

    def display(self):
        print("Name: " + self.name + "\nUSN: " + self.usn + "\nSubject 1:" + str(self.m1)+ "\nSubject 2:" + str(self.m2)+ "\nSubject 3:" + str(self.m3))

s1 = Student("Jay", "IS044", 40, 50, 50)
s1.calculate()
s1.display()