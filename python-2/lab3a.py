from random import randrange

#Simulated roll of the dice
def roll():
  dice1 = randrange(1,7)
  dice2 = randrange(1,7)
  total = dice1 + dice2

  #print "You rolled a {} ({} & {})".format(total,dice1, dice2)

  return dice1, dice2, total

rolls = 100000
stats = 13 * [0]

while rolls > 0:
  rolls -= 1
  dice1, dice2, total = roll()
  stats[total] += 1
 
for number in stats[2:]:
   percent = float(number) / 100000
   print "{} --> {:.2%}".format(stats.index(number),percent)
   

 
  
