"""Local/Global Demo Program

This program shows what variables are known in the main program
as well as the function.  It also demonstrates why you need to be
careful when modifying a global, immutable variable from a function.
Note how the global statement corrects the immediate problem.  If you
need to use this statement, you should review how you have written
this program. It is probably due for refactoring.

dir() poduces the names for that namespace.  local() poduces the namespace names
and values in the form of a dictionary.  The global statement allows
the function to act on global variables without causing problems for
the main program.  It is generally considered a crutch for bad code.

Run this program, and then uncomment the global statement and run
it again.  Note the difference in how the x variable is modified.
"""

from pprint import pprint
def lcl_tst(a, b):
    z = a + b
    print('Locals:')
    print(dir())
#    global x
    print('\nContents of Locals:')
    print(locals())
    x = 'changed'
    print('x =', x, '\n')
    return

x = 'string1'
y = 'string2'
lngint = 1234567890123456789
print('Globals:')
pprint(dir())
# print globals(), '\n'
print('\nContents of Globals:')
pprint(locals())
print('\n\n')
lcl_tst(x, y)
print('x =', x)
    
