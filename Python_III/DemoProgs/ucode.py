"""Unicode test for Python version 3

You get very different results in Python 2 vs 3 when
running this program even though the code is valid for both.
In Python 2 you need a declaration as well as other changes.
"""

x = '95\xb0'
print(x)
y = '95\u20ac'
print(y)
a = '95°'
print(a)
b = '95€'
print(b)
print('\n**From a literal')
print("""Comércio Mineiro
Berglunds snabbköp
Tradição Hipermercados""")
print('\n**From a file')
# fin = open('c:/pydata/latin.txt', encoding='latin-1')
fin = open('/home/bill/pydata/latin.txt', encoding='latin-1')
for datain in fin:
    print(datain, end='')

