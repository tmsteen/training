"""lab18a_imp.py

This program imports two classes: BankAccount and MinBalAcct.  This
avoids having to use dot notation to reference these two classes.
Note - class variables are still referenced through the original class.
"""

import sys
sys.path.append('/home/student/imports') # temporary addition to path
from banker import BankAccount, MinBalAcct

a = BankAccount()  # Create an instance of Bankaccount
b = BankAccount()  # Create another instance
print('Number of accounts -', BankAccount.acct_cntr)  # print class variable
del a
print('Number of accounts -', BankAccount.acct_cntr)
c = MinBalAcct(5000,1000)  # Create a minimum balance instance
print('Number of accounts -', BankAccount.acct_cntr)
print(c)
c.withdraw(4500)



