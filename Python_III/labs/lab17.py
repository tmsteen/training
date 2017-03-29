"""os and sys exercise

You may need to change the values of the
ds and di variables to get a meaningful result.
"""

import os, sys
ds = '/home/student/training/Python_III/words.txt' #directory with file
di = '/home/student/training/Python_III/'    #directory only
# ds = 'c:/pydata/words.txt'
# di = 'c:/pydata'

print(os.getcwd())
print(os.path.dirname(ds))
print(os.path.basename(ds))
print(os.path.exists(di))
print(os.path.isdir(ds))
print(os.path.isdir(di))
print(sys.argv)

from sys import path
print(path)
