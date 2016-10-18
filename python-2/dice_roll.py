"""
Title: Dice Roll
Author: Trevor Steen
Class: Python II

This program simulates a craps game.

Status 1 = Win
Status 2 = Lose
Status 3 = Continue
"""

from random import randrange

#Define starting amount of money
global bank
bank = 100

print "************************"

#Simulated roll of the dice
def roll():
  dice1 = randrange(1,7)
  dice2 = randrange(1,7)
  total = dice1 + dice2

  print "You rolled a {} ({} & {})".format(total,dice1, dice2)

  return dice1, dice2, total

#Initial roll, added logic to handle a win/loss on first roll
def comeout_roll(bank, bet):
  dice1, dice2, total = roll()
  bank = bank - bet

  if total == 7 or total == 11:
    print "You win!!!"
    status = 1
    bank = bank + bet * 2
  elif total == 2 or total == 3 or total == 12:
    print "You lose :("
    status = 2
  else:
    print "{} is now the point.".format(total)
    status = 3
    global point
    point = total

  return total, status, bank

#Subsequent rolls that win/lose on different parameters
def regular_roll(bank, bet):
  dice1, dice2, total = roll()

  if total == point:
    print "You win!!!"
    status = 1
    bank = bank + bet
  elif total == 7:
    print "You lose :("
    status = 2
  else:
    print "Rolling again..."
    status = 3

  return total, status, bank

#Do the first roll
first_roll, status, bank = comeout_roll(bank, 10)
print "Cash: {}".format(bank)

#Ask if user wants to continue
play_again = raw_input("Do you want to continue?")

#Determine if first roll was a win/lose, if not continue trying
while bank > 0 and play_again.lower() != 'n':
  if status == 2:
    first_roll, status, bank = comeout_roll(bank, 10)
    print "Cash: {}".format(bank)
  else:
    additional_roll, status, bank = regular_roll(bank, 10)
    print "Cash: {}".format(bank)

  play_again = raw_input("Do you want to continue? --> ") 
  
  
    
   
  








