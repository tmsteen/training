"""

This program demonstrates a very simple recursion
"""

def count_down(n):
    print(n)
    n -= 1
    if n == 0:
        print('Blastoff!')
        return
    count_down(n)

count_down(10)
