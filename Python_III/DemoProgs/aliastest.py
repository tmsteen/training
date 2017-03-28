"""
This code compares a list comprehension versus loops to create a
three-dimensional list with all entries set to zero. Then, it sets
one element to 5 to test for the creation of an alias.
"""

from pprint import pprint

# Using a comprehension
y = [[[0 for a in range(5)] for b in range(3)] for c in range(3)]
y[2][1][0] = 5
pprint(y)

print()

# Using loops
y = []
for c in range(3):
    tmplst1 = []
    for b in range(3):
        tmplst1.append(5 * [0])
    y.append(tmplst1)
y[2][1][0] = 5
pprint(y)
