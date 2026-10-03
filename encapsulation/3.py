# Create a class called Employee.

# Requirements:

# name → instance variable
# department → instance variable
# __salary → private instance variable
# Create get_salary() to return the salary.
# Create increase_salary(amount) to increase the salary.
# Create display() to show:
# Name
# Department
# Salary
# Create two employee objects with different details.
# Increase the salary of only one employee.
# Display both employees.
# Goal

# This assignment is mainly to practice:

# instance variable + private variable + encapsulation



class Employee:

    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.__salary=salary

    def get_salary(self):
        return self.__salary

    def increase_salary(self,amount):
        self.__salary+=amount

    def display(self):
        return "\nName : {}\nDepartment : {}\nSalary : {}".format(self.name,self.department,self.__salary)


e1=Employee("visnu","ai",30000)
e2=Employee("vardhan","ai",30000)

e1.increase_salary(5000)
print(e1.display())
print(e2.display())