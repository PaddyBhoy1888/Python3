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

# Dave.transfer(10000, Sara)
# Calls the transfer function using Dave account and sends the amount specified to Sara.
Dave.transfer(10, Sara)

Jim = InterestRewardsAcct(1000, "Jim")  # Creates a new account Jim

Jim.get_balance()  # Call Jims balance
Jim.deposit(100)  # Deposit 100 into Jims account
Jim.transfer(100, Dave)  # Transfer 100 to dave account from Jim account.

# Creates a new account 'Blaze' with amount and name
Blaze = SavingsAcct(1000, "Blaze")

Blaze.get_balance()  # Calls the balance for the account
Blaze.deposit(100)  # Calls the deposit function and adds 100
# Calls the transfer function and transfers 10000 to Sara account
Blaze.transfer(10000, Sara)
# Calls the transfer function and transfers 100 to Sara account
Blaze.transfer(100, Sara)
