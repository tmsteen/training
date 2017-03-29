"""lab13c_classvar.py

This class adds a class variable to keep track of the number of
accounts that have been created.
"""
import sys
sys.path.append('/home/student/training/Python_III/labs/accounts')

from Accounts import BankAccount, MinBalAccount

a = BankAccount()
a.deposit(200)
print(a)    

