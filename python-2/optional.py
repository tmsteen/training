"""
1-2 Month
3-4 Day
5-8 Year
9-13 Precip (dd.dd)
14-16 High Temp
"""

data = open('tmpprecip.dat')

weather_dict = dict()
average_dict = dict()

for day in data:
  # total rainfall, max temp, low temp, total days, cumm temp
  # initialize dictionary
  weather_dict[day[4:8]] = weather_dict.get(day[4:8],
                                            [0, 0, 1000, 0, 0])
  # accumulate rainfall
  weather_dict[day[4:8]][0] += float(day[8:13])
  #track highest temp
  if int(day[13:16]) > weather_dict[day[4:8]][1]:
    weather_dict[day[4:8]][1] = float(day[13:16])
  # track lowest temp
  if int(day[13:16]) < weather_dict[day[4:8]][2]:
    weather_dict[day[4:8]][2] = float(day[13:16])
  # track days
  weather_dict[day[4:8]][3] += 1
  # acummulate temp
  weather_dict[day[4:8]][4] += float(day[13:16])

  #initialize dictionary
  # month, cummulative rainfall
  average_dict[day[0:2]] = average_dict.get(day[0:2], 0)
  # total rainfall per month
  average_dict[day[0:2]] += float(day[8:13])

print("Year	Total	Max Temp Min Temp Avg Temp")
for year in sorted(weather_dict):
  print("{}  	{:5}  	{:5}  	{:5}  	{:.1f}".format(year,
                                      weather_dict[year][0],
                                      weather_dict[year][1],
                                      weather_dict[year][2],
                                      weather_dict[year][4] / 
                                      weather_dict[year][3]))
print "\n***********************\n"
for month in sorted(average_dict):
  print("{:4}  {:.2f}".format(month, average_dict[month] / len(weather_dict)))



  

