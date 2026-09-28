class ATM:
    def __init__(self):
        self.balance=10000
        self.pin=1234
        self.menu()
    def menu(self):
        user_input=input("""hello how can i help you ?
        1.set pin 
        2.change pin
        3.check balance
        4.wihdraw money 
        5.anything else
        """)

        if user_input=="1":
            self.set_pin()
        elif user_input=="2":
            self.change_pin()
        elif user_input=="3":
            self.check_balance()
        elif user_input=="4":
            self.withdraw_money()
        else:
            exit()

    def set_pin(self):
        new_pin=int(input("enter new pin"))
        self.pin=new_pin
        print("pin set successfully")
        self.menu()

    
    def change_pin(self):
        old_pin=int(input("enter old pin"))
        if old_pin==self.pin:
            new_pin=int(input("ener new pin:"))
            self.pin=new_pin
            print("pin changed successfully")
        else:
            print("enter correct pin")
        self.menu()

    def check_balance(self):
        user_pin=int(input("enter pin : "))
        if user_pin == self.pin:
            print("Balance : $",self.balance)
        else:
            print("enter correct pin!")
        self.menu()


    def withdraw_money(self):
        user_pin=int(input("enter pin : "))
        if user_pin == self.pin:
            amount=int(input("enter withdraw amount :"))
            if amount>self.balance:
                print("insufficient money")

            else:
                self.balance-=amount
                print("amount withdraw successfully")
        else:
            print("enter correct pin!")
        self.menu()
        

    
obj=ATM()
















