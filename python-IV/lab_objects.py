#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_objects` -- Objects in Python
=========================================

LAB Objects Learning Objective: Explore objects in Python and how everything in Python
                                is an object.

a. Fill in the series of functions below that determine the characteristics of an object.

b. Write a print_object_flags function that uses the is_* functions to find the characteristics
   of the passed in object and print the characteristics (flags).

"""


def is_callable(obj):
    """ returns True if the object is callable """
    # __call__
    return hasattr(obj, '__call__')



def is_with(obj):
    """ returns True if the object can be used in a "with" context """
    # __enter__, __exit__
    if hasattr(obj, '__enter__') or hasattr(obj, '__exit__'): return True
    else: return False


def is_math(obj):
    """ returns True if the object supports +, -, /, and * """
    # __add__, ...
    if (hasattr(obj, '__add__') or
    hasattr(obj, '__subtract__') or
    hasattr(obj, '__divide__') or
    hasattr(obj, '__multiply__')):
        return True
    else: return False


def is_iterable(obj):
    """ returns True if the object is iterable """
    # __iter__
    return hasattr(obj, '__iter__')


def print_object_flags(obj):
    """ assess the object for various characteristics and print them """
    print("Testing: ", obj)
    functions = [is_callable, is_with, is_math, is_iterable]
    for function in functions:
        print(function.__name__, ': ', function(obj))
    print("\n")
    pass


if __name__ == "__main__":
    print_object_flags(1)
    print_object_flags("abc")
    print_object_flags(print_object_flags)
    print_object_flags([1, 2, 3])
    print_object_flags(open('test.file.deleteme', 'w'))
