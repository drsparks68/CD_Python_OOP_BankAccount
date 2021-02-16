class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = 0
        self.balance = 0
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
yourAccount = BankAccount(0.0299, 500)