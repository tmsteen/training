book = open("/home/student/Python II Data/alice_in_wonderland.dat")
text = book.read().lower()

letter_count = 0
for letter in text:
  if letter.isalpha():
    letter_count += 1

e_count = text.count('e')

percent = float(e_count) / letter_count

print "Total Letters: {:.0f}".format(letter_count)
print "E's: {:.0f}".format(e_count)
print "Percent E's: {:.2f}%".format(percent*100)
