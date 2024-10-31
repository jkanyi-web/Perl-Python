class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited Ksh{amount:.2f}. New balance: Ksh{self.balance:.2f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew Ksh{amount}. Remaining balance: Ksh{self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def get_balance(self):
        return f"Account balance: Ksh{self.balance}"
      
# Derived class for Savings Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of Ksh{interest:.2f} applied. New balance: Ksh{self.balance:.2f}"
      
# Derived class for Checking Account
class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrew Ksh{amount}. Remaining balance: Ksh{self.balance}"
        else:
            return "Withdrawal amount exceeds balance and overdraft limit."
