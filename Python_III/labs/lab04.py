from string import punctuation
from operator import itemgetter

# Open and read files
with open('../alice_in_wonderland.dat') as book, open('../words.txt') as words:
    text = book.read().lower()

    # Create Dictionary
    word_dict = dict.fromkeys(words.read().splitlines(), 0)

# Create list to hold word not in list
missing_words = []

# Remove all punctuation
temp = str.maketrans(punctuation, ' ' * len(punctuation), "'")
text = text.translate(temp)

# Parse and Search
parsed = text.split()

for word in parsed:
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        missing_words.append(word)

# Calculate percentage used and most used
used_words = 0.0
highest = 0
most_used = ''
for word in word_dict:
    if word_dict[word] != 0:
        used_words += 1

word_list = set(zip(word_dict.keys(), word_dict.values()))
sorted_list = sorted(word_list, reverse=True, key=itemgetter(1))

percentage = used_words / len(word_dict) * 100
print("Words in dicitonary: {}".format(len(word_dict)))
print("Words in book: {}".format(len(parsed)))
print("Percentage of words used from the list is: {0:.5f}".format(percentage))

# Sort and dedup unfound list
print("\n")
print("Top 20 Most Used Words:".center(60))
print("\n")
print("Word:        Count:      ".center(60))
# print missing_words
for i in sorted_list[:20]:
    print("{:13s}{:13s}".format(i[0], str(i[1])).center(60))

