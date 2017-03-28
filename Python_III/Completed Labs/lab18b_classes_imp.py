"""lab18b_imp.py

This program imports only the module.  This requires every class
reference to be accessed through dot notation.  This includes all
references to class variables.

"""

import sys
sys.path.append('/home/student/imports') # temporary addition to path
import banker

a = banker.BankAccount()  # Create an instance of Bankaccount
b = banker.BankAccount()  # Create another instance
print('Number of accounts -', banker.BankAccount.acct_cntr)  # print class variable
del a
print('Number of accounts -', banker.BankAccount.acct_cntr)
c = banker.MinBalAcct(5000,1000)  # Create a minimum balance instance
print('Number of accounts -', banker.BankAccount.acct_cntr)
print(c)
c.withdraw(4500)



