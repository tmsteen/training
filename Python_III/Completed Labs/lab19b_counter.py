
from collections import Counter
from string import whitespace, punctuation

# eng_set = set(open('c:/pydata/words.txt').read().splitlines())
eng_set = set(open('/home/student/pydata/words.txt').read().splitlines())
# bookin = open('c:/pydata/alice_in_wonderland.dat').read().lower()
bookin = open('/home/student/pydata/alice_in_wonderland.dat').read().lower()
remove_chr = punctuation.replace("'", "") # remove the apostrophe
bookin = bookin.translate(str.maketrans(remove_chr, len(remove_chr) * ' ', "'"))
book_words = Counter(bookin.split())
print('Total words in book -', sum(book_words.values())) # Did it this way for demo purposes
print('Unique words in book -', len(book_words))
print(len(set(book_words) - eng_set), 'Book words not in dictionary')
for top_wrd, top_cnt in book_words.most_common(20):
    print('{0:.<10s}{1:,d}'.format(top_wrd, top_cnt))
