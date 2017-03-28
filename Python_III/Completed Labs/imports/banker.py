
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
    def __del__(self):
        BankAccount.acct_cntr -= 1

class MinBalAcct(BankAccount):
    def __init__(self, deposit, minbal):
        self.minimum_bal = minbal
        self.balance = deposit
        BankAccount.acct_cntr += 1
    def withdraw(self, amount):
        if self.balance - amount < self.minimum_bal:
            print('Withdrawal request of {:,.2f}'.format(amount))
            print('   denied due to minimum balance requirement')
        else:
            self.balance -= amount
    def __str__(self):
        return ("The balance for this account is ${:,.2f}\n" +
               "The minimum balance is ${:,.0f}").format(self.balance,
                                                        self.minimum_bal)    
        
