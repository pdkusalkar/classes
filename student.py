import sys
class Customer:
    '''' customer bank opertorions'''
    bankname="SBI"  #class variable or static variable
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposite(self,amt):
        self.balance=self.balance+amt
        print("bal after deposite",self.balance)

    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient balance funds..")
            sys.exit()
        self.balance=self.balance-amt
        print("Balance after withdraw",self.balance)

print("Welcome to ",Customer.bankname)
name=input("Enter your Name: ")
amount=float(input("Enter amount:"))
c=Customer(name,amount)
while True:
    print("d-Deposit\n w-withrow\n e-exit")
    option=input("Choose your option:")
    if option=='d' or option=='D':
        amt=float(input("Enter amount:"))
        c.deposite(amt)
    elif option=='w' or option=='W':
        amt=float(input("Enter amount"))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("Thanks for banking")
        sys.exit()
    else:
        print("Invalid option.. Please choose option")