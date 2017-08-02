#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

:mod:`lab_pyreview` -- Python review
=========================================

LAB PyReview Learning Objective: Review the topics from the previous courses

a. Load the data from the two dictionary files in the data directory into two
   list objects.  data/dictionary1.txt data/dictionary2.txt
   Print the number of entries in each list of words.

b. Use sets in Python to merge the two lists of words with no duplications (union).
   Print the number of words in the combined list.

c. Import the random library and use one of the functions to print out five random
   words from the combined list of words.

d. Use a list comprehension to find all the words that start with the letter 'a'.
   Print the number of words that begin with the letter 'a'.

e. Create a function called wordcount() with a yield that takes the list of
   all words as an argument and yields a tuple of
   (letter, number_of_words_starting_with_that_letter) with each iteration.

"""

##### a
dict1_list = []
dict2_list = []

with open('../data/dictionary1.txt', 'r') as dict1:
    for word in dict1:
        dict1_list.append(word)

with open('../data/dictionary2.txt', 'r') as dict2:
    for word in dict2:
        dict2_list.append(word)

print('Dictionary1 has ' + "{0:,g}".format(len(dict1_list)) + ' items.')
print('Dictionary2 has ' + "{0:,g}".format(len(dict2_list)) + ' items.')

##### b
dict1_set = set(dict1_list)
dict2_set = set(dict2_list)

union_set = set.union(dict1_set, dict2_set)

print("The union of unique values (set) is {0:,g} items".format(len(union_set)))

##### c
import random

newlist = []
for i in union_set:
    newlist.append(i)

print('Printing 5 random words')
for i in range(1,6):
    print(newlist[random.randrange(1,len(union_set))])

#### d
a_list = [word for word in newlist if word[0] == 'a']
print("Number of words that start with 'a': {0:,g}".format(len(a_list)))

##### e
def wordcount(wordlist):
    for i in wordlist:
        letter = i[0]
        letter_list = [word for word in wordlist if word[0] == letter]
        yield (letter, len(letter_list))

a = wordcount(newlist)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
