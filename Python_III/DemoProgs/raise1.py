"""Raise Standard Exceptions

Two ways to raise a standard exception and pass information to the
main program. Note the use of the args variable in returning
multiple items.
"""

def deposit1(amt):
    if amt < 1000:
        raise ValueError('Deposit too small' )
    else:
        print('Deposit OK')
    return

def deposit2(amt):
    if amt < 1000:
        raise ValueError('Deposit too small', amt) 
    else:
        print('Deposit OK')
    return

try:
    deposit1(100)
except ValueError as msg:
    print(msg)

try:
    deposit2(100)
except ValueError as msg:
    print(msg.args[0], '-', msg.args[1])
