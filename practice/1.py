# Assignment 1: Create a Student
# Easy

# Your task:

# Create a class called Student.

# Create an __init__() method that accepts a student's name and age.

# Use self to store the name and age as object attributes.

# Create an object for a student named "Vishnu", aged 20.

# Print the student's name and age.

# Expected output:

# Name: Vishnu
# Age: 20


class Student:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def display(self):
        return "name : {} , age : {}".format(self.name,self.age)

name=input("enter name :")
age=int(input("enter your age : "))
obj=Student(name,age)
print(obj.display())
