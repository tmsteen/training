"""lab13_eqmethod.py

Override the default __eq__ method so you can compare the balances of
two different accounts.  Change the amounts after the first execution.
"""

class BankAccount(object):  # Top tier class (super class)
    def __init__(self):   # This method runs during instantiation
        self.balance = 0  # instance variable 
    def withdraw(self, amount):  # a method
        self.balance -= amount
    def deposit(self, amount):     # another method
        self.balance += amount
    def __eq__(self, other):
        print('__eq__ method entered', self.balance, other.balance) 
        if self.balance == other.balance:
            return True
        return False

a = BankAccount()  # Create an instance of Bankaccount
b = BankAccount()  # Create another instance
a.deposit(2100)
b.deposit(2100)
if a == b:
    print('The two accounts have the same balance')
else:
    print('The balances are different')


