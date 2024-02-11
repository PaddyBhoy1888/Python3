# This is the OOP file that will draw the information from the bank_account example project

# From bank_accounts file import * (meaning imoport all)
from bank_accounts import *

# Creates an instance of a bankaccount with the name Dave. Draws on the class created in the bank_account file.
Dave = BankAccount(1000, "Dave")
# Creates an instance of a bankaccount with the name Sara
Sara = BankAccount(2000, "Sara")

# Calls the 'get_balance' function from the bank_account file within the BankAccount class.
Dave.get_balance()
Sara.get_balance()

Sara.deposit(500)  # Calls the 'deposit' function and inclueds a value.

Dave.withdraw(10000)
Dave.withdraw(10)
