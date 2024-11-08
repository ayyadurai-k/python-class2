class Bank:
    def __init__(self):
        self.amount = 0

    def deposit(self, amount):
        self.amount = self.amount + amount
        print(amount,"Deposited")

    def withdraw(self,amount):
        self.amount = self.amount - amount
        print(amount,"Withdrawn")
    
    def check_balance(self):
        print("Balance : ",self.amount)

account = Bank()
account.deposit(10000)
account.withdraw(5000)
account.check_balance()