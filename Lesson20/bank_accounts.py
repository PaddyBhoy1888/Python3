# This is a example project using classes & exceptions with object orientated programming "OOP"

class BalanceException(Exception):  # Defining the class that recieves an exception
    pass  # No code input so pass used.


class BankAccount:  # Creates a class called @BankAccount'
    # Using an initialisor function we can define variables to the 'BankAccount' class
    def __init__(self, initial_Amount, acct_Name):
        self.balance = initial_Amount
        self.name = acct_Name
        print(
            f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")
        # F string to give name & balance with balance to 2 decimal places

    # defines a function 'get_balance' inside the class.
    def get_balance(self):
        print(
            f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    # Define a function called 'deposit' insit the class that receieves 'self' & amount' values.
    def deposit(self, amount):
        self.balance = self.balance + amount  # This will define
        # print(
        #    f"\nDeposit Complete. \nAccount '{self.name}' Balance = ${self.balance:.2f}")
        print(
            "\nDeposit Complete")
        self.get_balance()

# For being able to withdraw moneis there has to be a way for the code to first check the balance and determine how much is in the account and how much is viable to be withdrawn.

    # Define a function called 'viable_transfer' which receives 'self & amount'
    def viable_transfer(self, amount):
        # If statement that will check 'self.balance' to see if the value is greater than or equal to the value asssigned to amount.
        if self.balance >= amount:
            return  # Then return the amount.
        else:  # Using elese if the value is less then raise an exception error with the defined statement.
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    # Defining the 'withdraw' function' inside the class where it recieves the 'self & amount' values.
    def withdraw(self, amount):
        try:  # Using a try we will check a few things below.
            # This will check the function 'viable_transfer' with the a defined input amount receieved. If no errors code will continue to the withdraw below and minus the amount from the account.
            self.viable_transfer(amount)
            # Here we check the self.balance where it is equal to the balance - the received amount above.
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")  # Print withdraw complete
            # Calls the 'get_balance' function to determine the remaining balance.
            self.get_balance()
        # Catch any errors and return the statement print and the error that has been detected.
        except BalanceException as error:
            print(f"\nWithdraw Interupted: {error}")

    # define transfer function with 'Self, amount & account' are inputs
    def transfer(self, amount, account):
        try:  # Try method to check the variables below
            # Short print statement to show the transfer has started
            print('\n******\n\n\Begining transfer..🚀')
            # Checks the amount stored against the amount input to make sure transfer can be made.
            self.viable_transfer(amount)
            self.withdraw(amount)  # Will run the withdraw function.
            # Will check the account specified and run the deposit function on that account
            account.deposit(amount)
            print('\nTransfer Complete! \n\n******')
        except BalanceException as error:
            print(f'\nTransfer Interupted. {error}')


# Creates a new class which inherites the parent class 'BankAccount'
class InterestRewardsAcct(BankAccount):

    def deposit(self, amount):  # Defines deposit function
        # Checks the self balance + the amount * 5%
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")  # Print statement
        self.get_balance()  # Check the balance of the account


# Creates a new class which inherites the parent class 'InterstRewardsAcct'
class SavingsAcct(InterestRewardsAcct):

    def __init__(self, initial_Amount, acct_Name):  # Defines function using the init function
        super().__init__(initial_Amount, acct_Name)
        self.fee = 5  # This adds a fee for anywithdraw

    def withdraw(self, amount):  # defines a new withdraw function inside tis class
        try:
            # Checks the amount + the fee set to see if enough funds in account
            self.viable_transfer(amount + self.fee)
            # Balance will be original ballance - (amount + Fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Complete.")
            self.get_balance()  # Calls the new balance

        except BalanceException as error:  # If an error accours return the error
            print(f"\nWithdraw Interupted: {error}")
