class Account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no
    def debit(self,amount):
        self.amount = amount
        self.balance -= amount
        print("Debit amount",amount)
    def credit(self,amount):
        self.amount =amount
        self.balance += amount
        print("Credit amount",amount)
    def print_balance(self):
        print("Balance:",self.balance)

a1=Account(10000,1)
a1.debit(100)
a1.print_balance()
a1.credit(100)
a1.print_balance()
