# Create a class called Rectangle.

# Requirements:

# __init__() should take length and width.
# Store them using self.
# Create a method called area() that calculates the area.
# Create a method called perimeter() that calculates the perimeter.
# Take length and width from the user.
# Create an object and display both results.

# Expected format:

# Enter length: 10
# Enter width: 5

# Area: 50
# Perimeter: 30



class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)


length=int(input("enter length : "))
width=int(input("enter width : "))
obj=Rectangle(length,width)
print("area :",obj.area())
print("perimeter :",obj.perimeter())