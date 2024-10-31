from bank_management_system import CheckingAccount
from bank_management_system import SavingsAccount

savings = SavingsAccount("123456", "Alice", 1000)
checking = CheckingAccount("789012", "Bob", 500)

# Deposit and withdraw from SavingsAccount
print(savings.deposit(200))          # Deposited $200. New balance: $1200
print(savings.apply_interest())      # Interest of $24.00 applied. New balance: $1224.00
print(savings.withdraw(300))         # Withdrew $300. Remaining balance: $924.00

# Deposit and withdraw from CheckingAccount
print(checking.deposit(100))         # Deposited $100. New balance: $600
print(checking.withdraw(650))        # Withdrew $650. Remaining balance: -$50
print(checking.get_balance())        # Account balance: -$50
