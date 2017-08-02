#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_subprocess` -- subprocess module
============================================

LAB subprocess Learning Objective: Familiarization with subprocess

::

 a. Use the subprocess run function to run "ls -l" and print the output.

 b. Do the same as a), but don't print anything to the screen.

 c. Do the same as a), but run the command "/bogus/command". What happens?

 d. Use subprocess Popen to run "du -h" and output stdout to a pipe. Read the pipe
    and print the output.

 e. Create a new function commander() which takes any number of commands to execute
    (as strings) on the arg list, then runs them sequentially printing stdout.

"""

import subprocess

#### Part A
subprocess.run(['ls', '-l'])

#### Part B
subprocess.run(['ls', '-l'], stdout=subprocess.DEVNULL)

#### Part C:
# subprocess.run(['command'])

#### Part Ds
subprocess.Popen(['du', '-h'], stdout=subprocess.PIPE)
print(subprocess.PIPE)

#### Part E
def commander(*arg):
    for i in arg:
        print("Output for {}".format(i))
        subprocess.run(i, shell=True)

commander('ls -al', 'du')
