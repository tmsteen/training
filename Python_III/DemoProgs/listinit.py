"""List Initialization

Initialize a 3-dimensional list with zeros using a comprehension.
The sample list is 5 x 3 x 3.  The process is meant to be generic.
The same process with loops is included for contrast.
"""

# Using a comprehension.
y = [[[0 for a in range(5)] for b in range(3)] for c in range(3)]
for x in y:
    print(x)
print()

# Using loops
y = []
for c in range(3):
    tmplst1 = []
    for b in range(3):
        tmplst2 = []
        for a in range(5):
            tmplst2.append(0)
        tmplst1.append(tmplst2)
    y.append(tmplst1)
for x in y:
    print(x)
