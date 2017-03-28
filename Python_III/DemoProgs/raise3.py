"""Raise Unique Exceptions

Create your own exception subclass inheriting from Exception.
You can add data that will be passed to the exception handler.
There are two ways to do this:
1) Actually place varaibles inside the instantiation
2) Return multiple arguments  as a tuple and access them through the class
   with dot notation through the args variable.
"""

class DepositError(Exception):
    pass   # No code is necessary but at least one statement is required
           # the pass statement satisfies that requirement and does nothing.
def deposit1(amt):    
    if amt < 1000:
        ex = DepositError('Deposit too small')
        ex.dep = amt
        ex.req = 1000
        raise ex  # The instance ex is passed to except on a
    else:         # DepositError
        print('Deposit OK')
    return

def deposit2(amt):    
    if amt < 1000:
        ex = DepositError('Deposit too small', amt, 1000)
        raise ex  # The instance ex is passed to except on a
    else:         # DepositError
        print('Deposit OK')
    return

try:
    deposit1(100)
except DepositError as err1:
    print(err1, '-', err1.dep, '  Need at least', err1.req)

try:
    deposit2(100)
except DepositError as err1:
    print(type(err1), len(err1.args), err1)  # err1 is actually a tuple
    print(err1.args[0], '-', err1.args[1], '  Need at least', err1.args[2])

