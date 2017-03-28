"""

This program uses recursion to sum the numbers in a simple list.

"""

def sum_it(n):
    print(n)
    if not n:
        return 0
    else:
        return n[0] + sum_it(n[1:])

x = [12, 3, 22, 18]
print(sum_it(x))
