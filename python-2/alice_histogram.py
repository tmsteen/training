from string import whitespace

book = open('alice_in_wonderland.dat')
text = book.read()

histogram = dict()

for letter in text:
  if letter not in whitespace:
    histogram[letter.lower()] = histogram.get(letter.lower(), 0) + 1

unload = zip(histogram.values(), histogram.keys())

unload.sort(reverse=True)

index = 0
while index < 29:
  try:
    print(unload[index][1] + ">" + str(unload[index][0]) + "\t"
    + unload[index + 1][1] + ">" + str(unload[index + 1][0])+ "\t"
    + unload[index + 2][1] + ">" + str(unload[index + 2][0])+ "\t"
    + unload[index + 3][1] + ">" + str(unload[index + 3][0])+ "\t"
    + unload[index + 4][1] + ">" + str(unload[index + 4][0]))

    index += 5
  except:
    break

'''
for i in unload[:30]:
  print(i[1] + " --> " + str(i[0]))

'''
