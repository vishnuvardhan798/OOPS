# # Create a class called ShoppingCart.

# # Requirements:

# # __init__() should create an empty list called items.
# # Create a method add_item(name, price, quantity) that adds a product to the cart.
# # Create a method remove_item(name) that removes a product from the cart.
# # Create a method calculate_total() that returns the total cost of all products.
# # Create a method display_items() that displays every product with:
# # Name
# # Price
# # Quantity
# # Take products from the user and add them to the cart.
# # Allow the user to remove a product.
# # Finally display all remaining products and the total price.

# # Example:

# # 1. Add item
# # 2. Remove item
# # 3. Display cart
# # 4. Calculate total
# # 5. Exit

# # This is the first assignment where you'll need to manage multiple objects/data inside a class.




class ShoppingCart:
    def __init__(self):
        self.items=[]
        self.menu()

    def menu(self):
        user=input("\n1.Add item \n2.Remove item \n3.display \n4.calculate total \n5.exit \nchoose one : ")
        if user=="1":
            self.add_item(input("enter item name :"),int(input("enter item price :")),int(input("enter item quantity :")))
        elif user=="2":
            self.remove_item(input("enter item name to remove : "))
        elif user=="3":
            self.display()
        elif user=="4":
            self.calculate_total()
        else:
            exit()



    def add_item(self,name,price,quantity):
        self.items.append({"name":name,"price":price,"quantity":quantity})
        self.menu()


    def remove_item(self,name):
        for item in self.items:
            if item["name"]==name:
                self.items.remove(item)
                print("item removed successflly")
                self.menu()
                return True
        print("item is there")
        self.menu()
        return False


    def display(self):
        for item in self.items:
            print("\nName:{}\nPrice:{}\nQuantity:{}".format(item["name"],item["price"],item["quantity"]))
        self.menu()


    def calculate_total(self):
        total=0
        for item in self.items:
            total+=item["price"]*item["quantity"]
        print("\nTotal : {}".format(total))

obj=ShoppingCart()






















# class ShoppingCart:
#     def __init__(self):
#         self.items=[]
#         self.menu()

#     def menu(self):
#         user_input=input("\n1.Add item \n2.Remove item\n3.Display\n4.Calculate toral\n5.exit\nchoose one : ")

#         if user_input=="1":
#             self.add_item(input("enter name :"),int(input("enter price:")),int(input("enter quantity :")))
#         elif user_input=="2":
#             self.remove_item(input("enter name :"))
#         elif user_input=="3":
#             self.display_cart()
#         elif user_input=="4":
#             self.calculate_total()
#         else:
#             exit()

#     def add_item(self,name,price,quantity):
#         self.items.append({"name":name,"price":price,"quantity":quantity})
#         self.menu()

#     def remove_item(self,n):
#         for item in self.items:
#             if item["name"]==n:
#                 self.items.remove(item)
#                 print("item removed succeessfully")
#                 self.menu()
#                 return True
#         print("item not found")
#         self.menu()
#         return False


#     def calculate_total(self):
#         total=0
#         for item in self.items:
#             total+=item["price"]*item["quantity"]
#         print("Total cost: {}".format(total))
#         self.menu()

#     def display_cart(self):
#         for item in self.items:
#             print("Name:{}\nPrice :{}\nQuantity:{}".format(item["name"],item["price"],item["quantity"]))
#         self.menu()

# obj=ShoppingCart()

















































# class ShoppingCart:
#     def __init__(self):
#         self.items=[]
#         self.menu()

#     def menu(self):
#         user_input=input("\n1.Add item \n2.Remove item\n3.Display\n4.Calculate toral\n5.exit\nchoose one : ")

#         if user_input=="1":
#             self.add_item(input("enter name :"),int(input("enter price:")),int(input("enter quantity :")))
#         elif user_input=="2":
#             self.remove_item(input("enter name :"))
#         elif user_input=="3":
#             self.display_cart()
#         elif user_input=="4":
#             self.calculate_total()
#         else:
#             exit()
    



#     def add_item(self,name,price,quantity):
#         self.items.append({"name":name,"price":price,"quantity":quantity})
#         self.menu()

#     def remove_item(self,n):
#         for item in self.items:
#             if item["name"]==n:
#                 self.items.remove(n)
#                 print("item removed succeessfully")
#                 self.menu()
#                 return True
#         print("item not found")
#         self.menu()
#         return False

#     def calculate_total(self):
#         total=0
#         for item in self.items:
#             total+=item["price"]*item["quantity"]
#         self.menu()

#     def display_cart(self):
#         for item in self.items:
#             print("Name:{}\nPrice :{}\nQuantity:{}".format(item["name"],item["price"],item["quantity"]))
#         self.menu()


# obj=ShoppingCart()