"""lab20_convert.py

Sample program to be used with 2to3 conversion. After the conversion,
note the changes to the zip function arguments.  Were they necessary?
Note, 2to3 does not deal with the changes to maketrans and translate.
You have to handle these manually.  
"""

from string import maketrans
from collections import Counter

dct = {x: ord(x) - 65 for x in 'ABCDEFG'}
abc = raw_input('Just enter something: ')
print 'Dictionary ',
print dct
lst = dct.items()
print 'List', lst
lst2 = sorted(lst)
lst3 = range(1, 11)
print lst2, '\n', lst3
dc_unload = zip(dct.values(), dct.keys())
print dc_unload
cntr = Counter('abracadabra')
cntr.subtract(list(cntr))
print cntr
cntr += Counter()
print cntr

test = 'random, text; in: use.'
trtbl = maketrans('aeiou', '?????')
print test.translate(trtbl, ',;:')
