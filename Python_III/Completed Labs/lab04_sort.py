"""lab04_sort.py

This program reads all of the words defined in the file words.txt and
creates a dictionary using each word as the key with an initial value of
zero.  Then it prints the number of entries in the dictionary.
It then reads in the entire book, "Alice in Wonderland,"
replaces all of the puctuation with either a space or a null character
and then splits on whitespace to isolate each word as an entry in a
list.  Then it proceeds to compare each word to the contents of the
dictionary keeping a count of each occurrence of each word that is used.
At the conclusion of processing the contents of the book, the number of
words in the English language dictionary and the number of words in the
book are both printed.  Then, the contents of the Python dictionary are
unloaded and sorted based on count.  Finally, the top 20 words are printed
in descending order by count.  Also, justification and fill are used to
format the words and their respective counts.
"""

from string import punctuation
from operator import itemgetter

punctuation = punctuation.replace("'", "")  # Remove the apostrophe
# with open('c:/pydata/words.txt', 'r') as fin:
with open('/home/student/pydata/words.txt', 'r') as fin:
    wordsin = fin.read().splitlines()
words = dict.fromkeys(wordsin, 0) # use the static method fromkeys
print('Words in dictionary - {0:,d}'.format(len(words)))

unfound_words = []  # List to keep words not located in dictionary.
# with open('c:/pydata/alice_in_wonderland.dat', 'r')as fin:
with open('/home/student/pydata/alice_in_wonderland.dat', 'r') as fin:
    bookin = fin.read().lower()

# Replace all punctuation except the ' with spaces.  remove all '
repl_punc = len(punctuation) * ' '
wordlist = bookin.translate(str.maketrans(punctuation, repl_punc, "'")).split()
print('Words in book - {0:,d}'.format(len(wordlist)))
for word in wordlist:
    if word in words:
        words[word] += 1  # If found, increment counter, otherwise
    else:
        unfound_words.append(word) # add to list of unfound words
unload_dict = words.items()  # unload dictionary into a list of
                             # key/value tuples
# Sort this list based on the 2nd entry in each tuple and then reverse
# the result.
sort_unload = sorted(unload_dict, key=itemgetter(1), reverse=True)
# or sort_unload = sorted(words.items(), key=itemgetter(1), reverse=True)
counter = 0  
for word, count in sort_unload:
    print('{0:.<13s}{1:,d}'.format(word, count))
    counter += 1
    if counter >= 20:  # Have we reached 20 items?
        break

print("\n\nWe're done!")


    
