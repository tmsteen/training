book = open("/home/student/Python II Data/alice_in_wonderland.dat")
text = book.read()

letter_count = 0.0
e_count = 0.0

for letter in text:
  if letter != ' ' and letter.lower() == 'e':
    e_count += 1
    letter_count += 1
  elif letter != ' ':
    letter_count += 1

percent = (e_count / letter_count) * 100

print "Total Letters: {:.0f}\nE's: {:.0f}\nPercent E's: {:.2f}%".format(letter_count, e_count, percent)
