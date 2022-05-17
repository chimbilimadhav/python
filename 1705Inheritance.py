# Create a class named Person, with firstname 
# and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

# use the Person class to create an object, and then execute the printname method:


class Student(Person):
    def __init__(self,fname,lname, year):
        super().__init__(fname,lname)      ## When we use super() function self keyword not required.
        self.graduationyear = year

    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to the class of", self.graduationyear)

x = Student("Madhav","Chimbili",2022)
x.welcome()