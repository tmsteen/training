"""lab20_convert.py

Sample program to be used with 2to3 conversion. After the conversion,
note the changes to the zip function arguments.  Were they necessary?
Note, 2to3 does not deal with the changes to maketrans and translate.
You have to handle these manually.  
"""

#  You will have to manually remove the following import:
#from string import maketrans  # maketrans no longer exists in string
from collections import Counter

dct = {x: ord(x) - 65 for x in 'ABCDEFG'}
abc = input('Just enter something: ')  # input replaces raw_input
print('Dictionary ', end=' ')  # print is now a fully-capable function
print(dct)
lst = list(dct.items()) # items is now an iterator, not a list
print('List', lst)
lst2 = sorted(lst)   # Sorted still produces a list - no change
lst3 = list(range(1, 11))  # range is also an iterator, replaces xrange
print(lst2, '\n', lst3)
# The following change is unnecessary.  zip works with all iterables.
# 2to3 tries to keep everything the same.  Since keys and values both
# produce iterables now, 2to3 makes lists out of them for consistency
# with the original code.
dc_unload = list(zip(dct.values(), dct.keys()))
print(dc_unload)
cntr = Counter('abracadabra')  # No changes to Counter or its
cntr.subtract(list(cntr))      # operators/methods.  There are
print(cntr)                    # some new capabilities
cntr += Counter()
print(cntr)

# In version 3, maketrans is now a static method and translate does
# not support delete characters.  Instead, you must use maketrans to
# create a dictionary that will delete the desired characters
test = 'random, text; in: use.'
#trtbl = maketrans('aeiou', '?????')
#print(test.translate(trtbl, ',;:'))

# The code that will work in Python 3 is as follows:
print(test.translate(str.maketrans('aeiou', '?????', ',;:')))
#  The objective of this code is to turn all vowels into question
#  marks and to delete all commas semicolons and colons.  Try the appropriate
#  sets of code in Python 2 and Python 3 respectively.  They should
#  do the same thing.
                                   
