from random import randint

rounds = 0
dups = 0



while rounds < 100000:
  students = 23
  birthdays = []

  while students > 0:
    birthdays.append(randint(1,365))
    students -= 1

  for i in range(1,366):
    if birthdays.count(i) > 1:
      dups += 1
      break

  rounds += 1

print("Percent of times with duplicate birthdays"
      + " is: {:.2%}".format(float(dups)/rounds))

    


