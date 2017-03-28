"""
The first test knows how many iterations are required to complete the
generator function.  It uses the generator as an iterable.  The second
test uses the next method and has to test for StopIteration to detect
when the generator has finished.  In this case, the results are the same.
"""

def yld_tst(cnt_dn):
    i = cnt_dn
    while i >= 0:
        yield i
        i -= 1

for z in yld_tst(10):  
    print(z)
print('yld_tst finished\n')
    
def yld_tst2(cnt_dn):
    i = cnt_dn
    while i >= 0:
        yield i
        i -= 1

nxt_gen = yld_tst2(10)
while True:
    try:
        print(nxt_gen.__next__())
    except StopIteration:
        print('yld_tst2 finished')
        break
