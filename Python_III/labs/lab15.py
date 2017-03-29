"""lab13c_classvar.py

This class adds a class variable to keep track of the number of
accounts that have been created.
"""

class BankAccount(object):  # Top tier class (super class)
    acct_cntr = 0         # class variable
    def __init__(self):   # This method runs during instantiation
        self.balance = 0  # instance variable
        BankAccount.acct_cntr += 1 # Accessing a class variable
    def withdraw(self, amount):  # a method
        self.balance -= amount
    def deposit(self, amount):     # another method
        self.balance += amount
    def __str__(self):
        return 'The balance for this account is ${:,.2f}'.format(
            self.balance)
    def __del__(self):  # Handles when an instance is deleted
        BankAccount.acct_cntr -= 1

class MinBalAccount(BankAccount):
    def __init__(self, min_bal, init_deposit):
        self.balance = 0
        BankAccount.acct_cntr += 1
        BankAccount.deposit(self, init_deposit)
        self.min_bal = min_bal
    def withdraw(self, amount):
        if self.balance - amount < self.min_bal:
            response = "[-] ERROR: Transaction Cancelled "
            response += "Insufficient funds to maintain minimum balance of {}".format(self.min_bal)
            print(response)
        else:
            self.balance -= amount
    def __str__(self):
        response = "The balance for this account is {:,.2f}, ".format(self.balance)
        response += "the minimum required balance is {:,.2f}".format(self.min_bal)
        return response
    

