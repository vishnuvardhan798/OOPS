# Create a class called Student.

# Requirements:

# Store the student's name and age.
# name and age should be instance variables.
# Create a method display() that prints the student's details.
# Create two different student objects with different names and ages.
# Display both students.

# Example type of output:

# Name: Vishnu
# Age: 21

# Name: Ravi
# Age: 20

# Don't use private variables or static/class variables yet.

class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        return "\nName:{}\nAge:{}".format(self.name,self.age)

obj1=Student("vishnu",19)
obj2=Student("vardhab",20)
print(obj1.display())
print(obj2.display())
