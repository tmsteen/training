file = open('/home/student/Python II Data/tmpprecip2012.dat')

precip_days = 0
precip_amount = 0

rain = '''

Art Credit:  Keith R. Fulton | keith.fulton@chinalake.navy.mil
       _
     _( )_          _     
   _(     )_      _( )_
  (_________)   _(     )_
    \  \  \    (_________)
      \  \       \  \  \
                   \  \


'''

for day in file:
  if float(day[8:13]) > 0:
    precip_days += 1
    precip_amount = precip_amount + float(day[8:13])

print rain
print "It rained {:d} days.".format(precip_days)
print "The total amount of rainfall was {:.2f}\n".format(precip_amount)

file.close()	 
