class Student:
    USN = ""
    name = ""
    sub1 = 0
    sub2 = 0
    sub3 = 0
    sub4 = 0
    def __init__(self, usn, name, l):
        self.USN = usn
        self.name = name
        self.sub1 = l[0]
        self.sub2 = l[1]
        self.sub3 = l[2]
        self.sub4 = l[3]
    def print_details(self):
        print("=================Student Details=================")
        print("USN: " + self.USN)
        print("Name: " + self.name)
        print("Subject 1: " + str(self.sub1))
        print("Subject 2: " + str(self.sub2))
        print("Subject 3: " + str(self.sub3))
        print("Subject 4: " + str(self.sub4))
    def calc(self):
        print("Average: " + str(int((self.sub1+self.sub2+self.sub3+self.sub4)/4)))

student1 = Student("1MS15IS044", "Jay", [80, 90, 70, 78])
student1.print_details()
student1.calc()