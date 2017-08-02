#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_args` -- Arguing with the functions
=========================================

LAB_ARGS Learning Objective: Learn to modify, receive, and work with arguments to function.
::

 a. Create a function that accepts any number of positional arguments and
    keyword arguments and prints the argument values out to the screen.

 b. Create a function that takes in any number of positional arguments, turns
    those arguments into keyword arguments using "arg#" for the keyword names,
    and calls the print function you wrote in a.

 c. Write a validation function that takes in a variable number of positional
    arguments.  Validate that all the arguments passed in are integers and are
    greater than 0.  If the arguments validate, call the print function, if an
    argument doesn't validate raise a ValueError.

"""

# Part A
def all_args(*args, **kwargs):
    for i in args:
        print(i)
    for i in kwargs:
        print(i, kwargs[i])

# Part B
def pos_args(*args):
    args_dict = {}
    arg_num = 0
    for i in args:
        arg_num += 1
        args_dict['arg{}'.format(arg_num)] = i

    all_args(args_dict)

# Part C
def validation(*args):
    valid_list = []
    for i in args:
        if isinstance(i, int) and i > 0:
            valid_list.append(i)
        else:
            raise ValueError('Args were not all integers')

    all_args(valid_list)
