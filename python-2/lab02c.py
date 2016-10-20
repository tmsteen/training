from string import printable

ascii_range = range(32, 127)
printable_chars = printable

for letter in ascii_range:
  print str(letter) + ' -- ' + chr(letter)

for letter in printable_chars:
  print "{!r} -- {}".format(letter, ord(letter))

