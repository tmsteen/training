gdp_list = open('../../gdp.txt').read().splitlines()

gdp_per_cap = []

for country in gdp_list:
  data = country.split(',')
  gdp_per_cap.append([data[0], (float(data[1]) 
                                / int(data[2])) * 1000000])

ordered_gdp = dict()

for i in gdp_per_cap:
  ordered_gdp.update({i[0]: i[1]})

unload = zip(ordered_gdp.values(), ordered_gdp.keys())
unload.sort(reverse=True)

for i in unload:
  print("{:20} ${:,.2f}".format(i[1], i[0])) 

print "\n********************************\n"

from string import punctuation

words = open('../../split.txt').read().lower().split()

words_no_punc = []

for i in words:
  for x in punctuation:
    i = i.replace(x,'')
  words_no_punc.append(i)

print("There are {} words".format(len(words_no_punc)))
words_set = set(words_no_punc)
print("There are {} unique words\n".format(len(words_set)))

word_list = []
for i in words_set:
  word_list.append(i)

word_list.sort()

for word in word_list:
  print word

