book = open('alice_in_wonderland.dat')
text = book.read().lower()

first_caterpillar = text.find('caterpillar')
first_gryphon = text.find('gryphon')
count_caterpillar = text.count( ' caterpillar')
count_gryphon = text.count('gryphon')
last_caterpillar = text.rfind('caterpillar')
last_gryphon = text.rfind('gryphon')

print "First occurance of 'caterpillar' at {} and appears {} times".format(first_caterpillar, count_caterpillar)

print "First occurance of 'gryphon' at {} and appears {} times".format(first_gryphon, count_gryphon)

print "Last occurences at: " + str(last_caterpillar) + ' ' + str(last_gryphon)
