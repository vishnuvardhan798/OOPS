# Create a class called Employee.

# Requirements:

# __init__() should take:
# name
# salary
# department
# Store them using self.
# Create a method display() to show all employee details.
# Create a method increase_salary(percentage) that increases the employee's salary by the given percentage.
# Create a method change_department(new_department) that changes the employee's department.
# Take all required information from the user.
# Create an object and perform both operations.

# Example:

# Enter name: Vishnu
# Enter salary: 30000
# Enter department: IT
# Enter salary increase percentage: 10
# Enter new department: AI

# Name: Vishnu
# Salary: 33000
# Department: AI

class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department

    def display(self):
        return "\nName : {}\nSalary : {}\nDepartment : {}".format(self.name,self.salary,self.department)

    def increase_salary(self,percentage):
        self.salary+=self.salary*percentage/100


    def change_department(self,new_department):
        self.department=new_department

obj=Employee(input("enter name :"),int(input("enter salary :")),input("enter department :"))
obj.increase_salary(int(input("enter salary increase percentage :")))
obj.change_department(input("enter new department :"))
print(obj.display())