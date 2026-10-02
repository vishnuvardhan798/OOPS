# Create a class called StudentManagement.

# Your program should manage multiple students.

# Each student should contain:

# Name
# Roll number
# Marks
# Methods required
# add_student()
# remove_student()
# search_student()
# display_students()
# calculate_average()
# find_topper()
# menu()
# Requirements
# add_student() should add a student's information to a collection.
# remove_student() should remove a student using their roll number.
# search_student() should search using the roll number and display that student's details.
# display_students() should display all students.
# calculate_average() should calculate the average marks of all students.
# find_topper() should find and display the student with the highest marks.
# The menu should keep running until the user exits.

# Menu:

# 1. Add Student
# 2. Remove Student
# 3. Search Student
# 4. Display Students
# 5. Calculate Average
# 6. Find Topper
# 7. Exit

# Example:

# 1. Add Student
# 2. Remove Student
# 3. Search Student
# 4. Display Students
# 5. Calculate Average
# 6. Find Topper
# 7. Exit

# Choose: 1

# Enter name: Vishnu
# Enter roll number: 101
# Enter marks: 85

# Student added successfully

# Important: Don't use a separate class for Student yet. Keep everything inside StudentManagement.


class StudentManagement:
    def __init__(self):
        self.students=[]
        self.menu()


    def menu(self):
        print("\n1. Add Student \n2. Remove Student\n3. Search Student\n4. Display Students\n5. Calculate Average\n6. Find Topper\n7. Exit")
        choose=input("choose your option :")

        if choose=="1":
            self.add_student(input("enter student name :"),int(input("enter roll no :")),int(input("enter marks :")))
        elif choose=="2":
            self.remove_student(int(input("enter student roll no to remove :")))
        elif choose=="3":
            self.search_student(int(input("enter rolll no :")))
        elif choose=="4":
            self.display_students()
        elif choose=="5":
            self.avg()
        elif choose=="6":
            self.find_topper()
        else:
            exit()
    

    def add_student(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    
        self.students.append({"name":name,"roll":roll,"marks":marks})
        print("student details added successfully")
        self.menu()

    def remove_student(self,roll):
        for student in self.students:
            if student["roll"]==roll:
                self.students.remove(student)
                print("student removed successfully")
                self.menu()
                return True
        print("student is not there")
        self.menu()
        return False

    def search_student(self,roll):
        for student in self.students:
            if student["roll"]==roll:
                print("\nName:{}\nROll NO:{}\nMarks:".format(student["name"],student["roll"],student["marks"]))
                self.menu()
                return True
        print("there is no student with that roll no")
        self.menu()
        return False

    
    def avg(self):
        self.total=0
        for student in self.students:
            self.total+=student["marks"]
        self.average=self.total/len(self.students)
        print("\nAverage marks:{}".format(self.average))
        self.menu()


    def find_topper(self):
        self.topper=max(self.students,key=lambda x:x["marks"])
        print("\nName:{}\nRollno:{}\nMarks:{}".format(self.topper["name"],self.topper["roll"],self.topper["marks"]))
        self.menu()

    def display_students(self):
        for student in self.students:
            print("\nName:{}\nRollno:{}\nMarks:{}".format(student["name"],student["roll"],student["marks"]))
        self.menu()

    
obj=StudentManagement()
            

            
