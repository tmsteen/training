#!/bin/python3

from string import whitespace, punctuation
from collections import Counter

with open('../alice_in_wonderland.dat') as book:
    text = book.read().lower()
    
with open('../words.txt') as wordlist:
    wlist = wordlist.read().lower()
 
def char_count(top_count):
    removal = str.maketrans('', '', whitespace)
    no_white = text.translate(removal)    
        
    histogram = Counter(no_white)
        
    print("Most Common Characters".center(60))
    for i in histogram.most_common(top_count):
        graph = '-' * (int(i[1])//100)
        print("{}{}{}".format(i[0], graph, i[1]))
        

def word_count(top_count):
    removal_punct = str.maketrans(punctuation, ' ' * len(punctuation), "'")
    no_punct = text.translate(removal_punct)
    
    words = no_punct.split()
    
    total_words = len(words)
    unique_words = len(set(words))
    
    histogram = Counter(words)
    
    not_in_list = []
    for i in histogram:
        if i not in wlist:
            not_in_list.append(i)
    
    num_not_in_list = len(not_in_list)
    
    top_x = histogram.most_common(top_count)
    
    print('Total Words: {}'.format(total_words))
    print('Unique Words: {}'.format(unique_words))
    print('Words Not In List: {}'.format(num_not_in_list))
    print("Most Common Words".center(60))
    for i in top_x:
        graph = '-' * (int(i[1])//10)
        print("{}{}{}".format(i[0], graph, i[1]))


char_count(20)

print()
print ('###########################################################3')
print()
word_count(20)
