"""Sort with random results

This sort creates a tempprecip file that is not ordered chronologically.
"""

from random import randrange as rr
tmprecs = list(open('c:/pydata/tmpprecip2.dat', 'r'))
tmprecs.sort(key=lambda x: rr(1,100001))
open('c:/pydata/unorderedtmps.dat', 'w').writelines(tmprecs)
