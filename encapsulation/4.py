# Now we'll introduce a class variable.

# Create a class called Student.

# Requirements:

# school_name = "ABC School" → class variable
# name → instance variable
# age → instance variable
# __marks → private instance variable
# Create get_marks() to return the marks.
# Create display() that shows:
# Student name
# Age
# School name
# Marks
# Create 3 student objects with different names, ages, and marks.
# Print the details of all 3 students.
# Change the school name using the class, so the new school name is displayed for all 3 students.

# Focus: instance variable + class variable + private variable + encapsulation.

class Student:
    college_name="ABC School"

    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.__marks=marks

    def get_marks(self):
        return self.__marks

    def display(self):
        return "\nName : {}\nAge : {}\nMarks : {}\nCollege Name : {}".format(self.name,self.age,self.__marks,Student.college_name)

Student.college_name="kec"
s1=Student("v",19,99)
s2=Student("s",20,98)
s3=Student("vv",20,98)

print(s1.display())
print(s2.display())
print(s3.display())