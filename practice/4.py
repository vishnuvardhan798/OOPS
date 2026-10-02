# Create a class called BankAccount.

# Requirements:

# __init__() should take:
# account_holder
# balance
# Store them using self.
# Create a method deposit(amount) that adds money to the balance.
# Create a method withdraw(amount) that subtracts money from the balance.
# Create a method display_balance() that displays the current balance.
# Take the account holder and initial balance from the user.
# Take a deposit amount and withdraw amount from the user.
# Create an object and perform the operations.

# Example:

# Enter account holder: Vishnu
# Enter initial balance: 10000
# Enter deposit amount: 2000
# Enter withdraw amount: 3000

# Account Holder: Vishnu
# Final Balance: 9000

class BankAccount:
    def __init__(self,act_holder,balance):
        self.account_holder=act_holder
        self.pin=1234
        self.balance=balance
        self.menu()


    def menu(self):
        user_input=input("how can i help you ? \n1.set pin \n2.change pin \n3.check balance \n4.deposit money \n5.withdraw money \n6.exit \n")

        if user_input=="1":
            self.set_pin()
        elif user_input=="2":
            self.change_pin()
        elif user_input=="3":
            self.check_balance()
        elif user_input=="4":
            self.deposit_money() 
        elif user_input=="5":
            self.withdraw_money()
        else:
            exit()


    def set_pin(self):
        new_pin=int(input("enter new pin : "))
        self.pin=new_pin
        print("pin set successfully")
        self.menu()
    def change_pin(self):
        old_pin=int(input("enter old pin : "))
        if old_pin==self.pin:
            new_pin=(int(input("enter new pin :")))
            self.pin=new_pin
            print("pin changed successfully")
            self.menu()
        else:
            print("wrong pin! try again")
            self.menu()

    def check_balance(self):
        user_pin=int(input("enter pin : "))
        if user_pin==self.pin:
            print("balance : $",self.balance)
            self.menu()
        else:
            print("wrong pin! try again")
            self.menu()

    def deposit_money(self):
        user_pin=int(input("enter pin : "))
        if user_pin==self.pin:
            amount=int(input("enter deposit amount : "))
            self.balance+=amount
            print("amount deposited successfully")
            self.menu()
        else:
            print("wrong pin! try again")
            self.menu()

    def withdraw_money(self):
        user_pin=int(input("enter pin : "))
        if user_pin==self.pin:
            amount=int(input("enter withdraw amount :"))
            if amount>self.balance:
                print("insufficient money")
                self.menu()
            else:
                self.balance-=amount
                print("amount withdraw successfully")
                self.menu()
        else:
            print("wrong pin! try again")
            self.menu()

obj=BankAccount(input("enter account holder : "),int(input("enter initial balance : ")))


    