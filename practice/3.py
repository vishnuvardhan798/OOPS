# Create a class called Car.

# Requirements:

# __init__() should take:
# brand
# model
# price
# Store all three using self.
# Create a method display() that displays all car details.
# Take all three values from the user.
# Create an object and call display().

# Expected output:

# Enter brand: Toyota
# Enter model: Camry
# Enter price: 2500000

# Brand: Toyota
# Model: Camry
# Price: 2500000


class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        return 'Brand : {} , model : {} , price : {}'.format(self.brand,self.model,self.price)

brand=input("enter brand:")
model=input("enter model :")
price=int(input("enter the price :"))
obj=Car(brand,model,price)
print(obj.display())