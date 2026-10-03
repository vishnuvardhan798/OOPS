# Create a class called BankAccount.

# Requirements:

# bank_name = "ABC Bank" → class variable
# account_count = 0 → class variable
# name → instance variable
# __balance → private instance variable
# Every time a new account is created, increase account_count by 1.
# Create deposit(amount).
# Create withdraw(amount).
# Create get_balance().

# Create a static method called bank_info() that prints:

# Welcome to ABC Bank
# Create 3 accounts.
# Perform deposits/withdrawals on different accounts.
# Display the final balance of each account.
# Call bank_info() without creating another object.
# Finally, display the total number of accounts created.
# Concepts you're now combining:

# Class variable + instance variable + private variable + encapsulation + static method

class BankAccount:
    bank_name="ABC Bank"
    account_count=0

    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
        BankAccount.account_count+=1

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        if amount<self.__balance:
             
            self.__balance-=amount
        else:
            print("insufficient money")

    @staticmethod
    def bank_info():
            print("welcome to  {}".format(BankAccount.bank_name))
    


a1=BankAccount("v",1000)
a2=BankAccount("vv",2000)
a3=BankAccount("s",2500)

a1.deposit(1000)
a2.deposit(2000)
a3.deposit(2500)

a1.withdraw(500)
a2.withdraw(500)
a3.withdraw(500)

print(a1.get_balance())
print(a2.get_balance())
print(a3.get_balance())

BankAccount.bank_info()
print("accounts :",BankAccount.account_count)



    