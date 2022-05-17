"""
Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. 
Eg.: Myclass.Myattribute
"""
# Class objects
"""
An Object is an instance of a Class. A class is like a blueprint 
while an instance is a copy of the class with actual values. 
It is not an idea anymore.
"""
# An object consists of :
"""State: It is represented by the attributes of an object. 
It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. 
It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and 
enables one object to interact with other objects.
"""

# program to import built-in array module and
#  display the namespace of the said module

import array
for name in array.__dict__:
    print(name)

# program to create a class and display the namespace of the said class.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
ModelX = Vehicle(240,24)
print("Speed of the Vehicle is:",ModelX.max_speed,"\nMileage of the vehicle is:",ModelX.mileage)

# Create a Vehicle class without any variables and methods

"""class Vehicle:
    pass
"""
class Bus(Vehicle):
    def __init__(self, name,max_speed, mileage):
        super().__init__(max_speed, mileage)
        self.name = name

school_bus = Bus('Volvo',240,24)
print("Vehilce_Name:",school_bus.name,school_bus.mileage,school_bus.max_speed)

class Vehicle:

    color ='white'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self, capacity):
        return f"The Seating capacity of {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity = 50,):
        return super().seating_capacity(capacity=50)
    
class car(Vehicle):
    pass

school_bus = Bus("Volvo School Bus", 240,24)
print(school_bus.seating_capacity())

print(school_bus.color,school_bus.name,school_bus.max_speed,school_bus.mileage)

Car = car("VW POLO", 240, 18)

print(Car.color,Car.name,"Speed:",Car.max_speed,"Mileage:", Car.mileage)

############ CALCULATE BUS FARE ####################

class Vehicle:
    def __init__(self,name,mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount
        
school_bus = Bus("School_volvo", 12, 50)

print("Total Bus Fare is:", school_bus.fare())
print(type(school_bus))
print(isinstance(school_bus, Vehicle))

#  program which import the abs() function using the builtins module, 
# display the documentation of abs() function and find the absolute value of -155.

import builtins
help(builtins.abs)
print(builtins.abs(-155))

#  Define a Python function student(). 
# Using function attributes display the names of all arguments.

def student(student_id,student_name,student_class):
    return f'Student_id:{student_id}\nStudent_Name: {student_name}\nStudent_class: {student_class}'

print(student(134,'DEVANSHI','LKG'))

# Python function FOR student_data () 
# which will print the id of a student (student_id). 
# If the user passes an argument student_name or student_class 
# the function will print the student name and class

def student_data(student_id, **kwargs):
    print(f'\nStudent Id: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")
    if 'student_name' and 'student_class' in kwargs:
        print(f"\nStudent name: $ {kwargs['student_name']}")
        print(f"\nStudent Class: $ {kwargs['student_class']}")

student_data(student_id=134, student_name = 'Devanshi madhav')

student_data(student_id=134, student_name = "madhav chimbili", student_class = 'VI' )

# Python class named Student and display its type. 
# Also, display the __dict__ attribute keys and
# the value of the __module__ attribute of the Student class.
class Student:
    pass
print("Type is:",type(Student))
print("Keys:",Student.__dict__.keys())
print("Module is:", Student.__module__)


# Write a Python program to crate two empty classes, Student and Marks. 
# Now create some instances and check whether they are instances of the said classes or not. 
# Also, check whether the said classes are subclasses of the built-in object class or not.

class Student:
    pass
class Marks:
    pass

student1 = Student()
marks1 = Marks()
print("\nCheck whether the said classes are subclasses of the built in object class or not")
print(isinstance(student1, Student))
print(isinstance(Student, Marks))
print(isinstance(marks1, Marks))
print(isinstance(marks1, Student))
print("\nCheck whether the said classes are subclasses of the built in object class or not")
print(issubclass(Student, object))
print(issubclass(Marks, object))
