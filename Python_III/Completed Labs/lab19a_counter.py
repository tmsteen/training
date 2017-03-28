"""lab19_counter.py

This program counts the number of times each character (except whitespace)
is used in the book, "Alice in Wonderland."  It is an example of using
the translate method in conjunction with the maketrans function.  In this
case maketrans is used to create the standard 256-byte table with no
changes.  Translate is used to delete the whitespace.  Then, the Counter
class (imported from collections) is instantiated with the translated
book as input.  After that, the most_common method is used to print the
top 20 characters.
"""

from string import whitespace
from collections import Counter

# bookin = open('c:/pydata/alice_in_wonderland.dat', 'r').read().upper()
bookin = open('/home/student/pydata/alice_in_wonderland.dat',
              'r').read().upper()
# Use translate with a default table just to remove white space and punctuation.
trbookin = bookin.translate(''.maketrans('', '', whitespace))
x = Counter(trbookin) # instantiate Counter with the book as input
# print the 20 most common letters in the book
for i, j in x.most_common(20):
    print('{0} {1:6,d}'.format(i, j))  
