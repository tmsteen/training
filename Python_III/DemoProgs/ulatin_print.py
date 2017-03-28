"""Latin characters

This loop prints all of the latin characters.  Note it skips the first
34 characters as those are special use.
"""

for latchr in range(161, 256):
    print(chr(latchr), end=' ')
