# Create a class called BankAccount.

# Requirements:

# name → instance variable.
# balance → private instance variable.
# Create a deposit(amount) method.
# Create a withdraw(amount) method.
# Create a get_balance() method to return the private balance.
# Create two bank account objects with different names and balances.
# Deposit money into one account.
# Withdraw money from the other account.
# Display the final balance of both accounts.

# Important: Do not directly access the private balance outside the class.


class BankAccount:

    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def __str__(self):
        return "\nName : {}".format(self.name)

    def get_balance(self):
        return self.__balance

    def deposit(self):
        amount=int(input("enter deposit amount :"))
        self.__balance+=amount
        print("amount added successfully")

    def withdraw(self):
        self.amount=int(input("enter withdraw amount :"))
        if self.amount>self.__balance:
            print("insufficient money")
        else:
            self.__balance-=self.amount
            print("withdraw successfull")

p1=BankAccount("vishnu",10000)
p2=BankAccount("vardhan",10000)

p1.deposit()
p2.withdraw()
print(p1.get_balance())
print(p2.get_balance())
    
