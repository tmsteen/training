from string import printable

ascii_range = range(32, 127)
printable_chars = printable

for letter in ascii_range:
  print chr(letter)

for letter in printable_chars:
  print "{!r}".format(ord(letter))

