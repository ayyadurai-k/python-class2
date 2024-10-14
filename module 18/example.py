

class BankAccount:
    def deposit_amount(self):
        self.deposit_amount = int(input("Enter amount to deposit : "))

    def calculate_interest(self):
        interest = self.deposit_amount * 0.02  # 2 %
        print("Interest : ",interest)

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        interest = self.deposit_amount * 0.04  # 4 %
        print("Interest : ",interest)

class DepositAccount(BankAccount):
    def calculate_interest(self):
        interest = self.deposit_amount * 0.07  # 7 %
        print("Interest : ", interest)


account = SavingsAccount()

account.deposit_amount()

account.calculate_interest()