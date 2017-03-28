"""lab03_translate.py

This program reads all of the words defined in the file words.txt and
creates a dictionary using each word as the key with an initial value of
zero.  It does this by using the fromkeys method.
It then reads in the entire book, "Alice in Wonderland,"
replaces all of the punctuation with either a space or a null character
using the translate method along with the maketrans function
and then splits on whitespace to isolate each word as an entry in a
list.  Then it proceeds to compare each word to the contents of the
dictionary keeping a count of each occurrence of each word that is used.
If a word isn't found, it is appended to a list of unfound words.  At
the end it calculates and prints the percentage of dictionary words that
were used in the book, the word that was used the most along with the
number of occurrences and finally, it removes the duplicates from the
unfound words list and prints the result in alphabetical order.

This version of the program uses translate/maketrans instead of
the replace method in a loop.
"""

from string import punctuation

punctuation = punctuation.replace("'", "")  # Remove the apostrophe
# with open('c:/pydata/words.txt', 'r') as fin:
with open('/home/student/pydata/words.txt', 'r') as fin:
    wordsin = fin.read().splitlines()
    words = dict.fromkeys(wordsin, 0) # use the static method fromkeys
print('Words in dictionary - {0:,d}'.format(len(words)))

unfound_words = []  # List to keep words not located in dictionary.
# with open('c:/pydata/alice_in_wonderland.dat', 'r') as fin:
with open('/home/student/pydata/alice_in_wonderland.dat', 'r') as fin:
    bookin = fin.read().lower()  # read entire book; lower the case

# Replace all punctuation except the ' with spaces.  remove all '
tr_table = str.maketrans(punctuation, len(punctuation) * ' ', "'")
bookin = bookin.translate(tr_table)
wordlist = bookin.split()
print('Words in book - {0:,d}'.format(len(wordlist)))
for word in wordlist:
    if word in words:
        words[word] += 1  # If found, increment counter, otherwise
    else:
        unfound_words.append(word) # add to list of unfound words

wordlist2 = sorted(zip(words.values(), words.keys()))
max_times, max_word = wordlist2[-1]

# Calculate the percentage of dictionary words used in the book.
unused_words = list(words.values()).count(0) # number of words with a zero count
print('Percentage of dictionary words used in the book is {0:.2%}'.format(
    float(len(words) - unused_words) / len(words)))
print('The word "{0}" was the most frequently used at {1:,d} times'.format(
    max_word, max_times))
# Remove duplicates from unfound list and sort the result
unique_unfound = sorted(set(unfound_words))
print('Number of book words not found in the dictionary -', len(unique_unfound))
nuline = 0
# Print each word left justified in 13 character spaces, and
# put five words on a line.
print('\n{0}\n'.format('Unfound Words'.center(60)))
for word in unique_unfound:
    print('{0:13s}'.format(word), end=' ')
    nuline += 1
    if nuline >= 5:
        nuline = 0
        print()

print("\n\nWe're done!")


    
