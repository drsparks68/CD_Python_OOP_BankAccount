class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging $5 fee")
            return self
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Account balance is: {self.balance}")
    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance =  self.balance + interest
        return self

myAccount = BankAccount(0.0199, 1000)
myAccount.deposit(57.63).deposit(34.23).deposit(404.00).yield_interest().display_account_info()

yourAccount = BankAccount(0.0299, 500)
yourAccount.withdraw(12.67).withdraw(37.66).deposit(372.00).withdraw(400.07).deposit(1100.17).withdraw(307.68).yield_interest().display_account_info()

