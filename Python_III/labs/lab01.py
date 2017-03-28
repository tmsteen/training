from string import whitespace
from string import punctuation

# Open and read files
book = open('../alice_in_wonderland.dat')
words = open('../words.txt')
text = book.read().lower()

# Create Dictionary
word_dict = {}
for word in words:
    word = word.replace("\r", '')
    word = word.replace("\n", '')
    word_dict[word] = 0

# Create list to hold word not in list
missing_words = []

# Remove all punctuation
for char in punctuation:
    text = text.replace(char, '')

for char in whitespace:
    text = text.replace(char, ' ')

# Parse and Search
parsed = text.split(' ')

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
        if word_dict[word] > highest:
            most_used = word
            highest = word_dict[word]

percentage = used_words / len(word_dict) * 100.0
print("Words in dicitonary: {}".format(len(word_dict)))
print("Words in book: {}".format(len(parsed)))
print("Percentage of words used from the list is: {0:.5f}".format(percentage))
print("Most used word is: '{}' with {} hits.".format(most_used, highest))

# Sort and dedup unfound list
print("Words not in dictionary:")

# print missing_words
missing_words.sort()
unique_missing = set(missing_words)
print(unique_missing)
