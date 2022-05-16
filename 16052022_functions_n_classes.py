class Child():

    #  constructor
    def __init__(self,name):
        self.name = name
    # to get name
    def getName(self):
        return self.name
    def isStudent(self):
        return False
class Student(Child):
    def isStudent(self):
        return True

#  Driver Code
#  An Object of child

std = Child("Madhav")
print(std.getName(),std.isStudent())

#  An Object of Student

std = Student("Devanshi")
print(std.getName(),std.isStudent())

class Mother:
    mothername = " "
    def mother(self):
        print(self.mothername)
class Father:
    fathername = " "
    def father(self):
        print(self.fathername)
class Daughter(Father, Mother):
    daughtername = " "
    def daughter(self):
        print(self.daughtername)
    def Parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
        print("Daughter: ",self.daughtername)

d = Daughter()
d.fathername = "MADHAV"
d.mothername = "SRAVANI"
d.daughtername = "DEVANSHI"
d.Parents()