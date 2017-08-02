#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

:mod:`lab_decorators_with_parameters` --- Decorators with parameters practice
========================================

a. Modify the decorator you created in the lab_decorators.py to accept an argument
   that specifies whether to print the timing in seconds or milliseconds.  Make the
   default units seconds.

"""

import time

def timer(seconds=True):
    def real_timer(func):
        def inner(item):
            start_time = time.time()
            retval = func(item)
            stop_time = time.time()
            elapsed = stop_time - start_time
            if seconds:
                print(elapsed, ' s')
            else:
                print(elapsed * 1000, ' ms')
            return retval
        return inner
    return real_timer

@timer(seconds=False)
def time_me(item):
    """time this function for various calls"""
    def is_prime(num):
        for j in range(2, num):
            if (num % j) == 0:
                return False
        return True

    index = 0
    check = 0
    while index < item:
        check += 1
        if is_prime(check):
            index += 1
    return check


if __name__ == "__main__":
    for step in range(10):
        # run your decorated function instead
        time_me(200)
