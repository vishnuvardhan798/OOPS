# Create a class called Product.

# Requirements
# store_name = "Vishnu Store" → class variable
# product_count = 0 → class variable
# name → instance variable
# price → instance variable
# __stock → private instance variable
# Increase product_count whenever a new product is created.
# Create add_stock(quantity) to increase stock.
# Create sell(quantity) to decrease stock.
# Create get_stock() to return the private stock.
# sell() should not allow selling more than the available stock.
# Create a display() method showing:
# Product name
# Price
# Current stock
# Store name
# Create a static method store_info() that prints the store name.
# Create at least 2 products and perform different stock operations on them.
# Display the final details of both products.
# Main goal

# This time pay attention to the difference between:

# product_count → shared by all products
# __stock      → separate for every product
# price        → separate for every product

class Product:
    store_name="Vishnu Store"
    product_count=0

    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.__stock=stock
        Product.product_count+=1

    def add_stock(self,quantity):
        self.__stock+=quantity

    def sell_stock(self,quantity):
        if quantity<=self.__stock:
            self.__stock-=quantity
        else:
            print("insufficient stock")

    def get_stock(self):
        return self.__stock

    def display(self):
            print("\nProduct Name : {}\nPrice : {}\nCurrent Stock : {}\nStore Name: {}".format(self.name,self.price,self.__stock,Product.store_name))

    @staticmethod
    def get_info():
        print("\nStore Name :{}\nProduct Count: {}".format(Product.store_name,Product.product_count).upper())


product1=Product("biscuit",10,100)
product2=Product("chocolate",5,100)
product3=Product("chips",5,100)

products=[product1,product2,product3]

product1.add_stock(50)
product2.sell_stock(30)

for product in products:
    product.display()

print(Product.get_info())




# product1=Product("biscuit",10,100)
# product2=Product("chocolate",5,100)

# product1.add_stock(50)
# product2.sell_stock(30)

# product1.display()
# product2.display()

# Product.get_info()