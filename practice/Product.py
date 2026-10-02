# Create a class called Product.

# Requirements:

# __init__() should take:
# name
# price
# quantity
# Create a method total_price() that returns:
# price × quantity
# Create a method apply_discount(percentage) that reduces the price by the given percentage.
# Create a method display() that shows:
# Product name
# Price after discount
# Quantity
# Total price
# Take all values from the user.
# Create an object and call the methods.

# Example:

# Enter product name: Laptop
# Enter price: 50000
# Enter quantity: 2
# Enter discount percentage: 10

# Product: Laptop
# Price: 45000
# Quantity: 2
# Total Price: 90000

class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_price(self):
        return self.price*self.quantity

    def apply_discount(self,percentage):
        self.price=self.price-(self.price*percentage/100)

    def display(self):
        return "\nProduct :{}\nPrice : {}\nQuantity :{}\nTotal Price :{}".format(self.name,self.price,self.quantity,self.total_price())

obj=Product(input("enter product name :"),int(input("enter price :")),int(input("enter quantity :")))
obj.apply_discount(int(input("enter the discount percentage :")))
print(obj.display())