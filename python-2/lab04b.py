data_100yr = open('/home/student/Python II Data/tmpprecip.dat')
data_2012 = open('/home/student/Python II Data/tmpprecip2012.dat')

def data_parser(data):
  # initialize list
  table = []
  for i in range(13):
    table.append([0, 0, 0, 1000]) # month, total, high, low

  for day in data:
    table[int(day[0:2])][0] += 1  # set days
    table[int(day[0:2])][1] += int(day[13:16])  # sum temp

    if int(day[13:16]) < int(table[int(day[0:2])][3]):
      table[int(day[0:2])][3] = int(day[13:16])

    if int(day[13:16]) > int(table[int(day[0:2])][2]):
      table[int(day[0:2])][2] = int(day[13:16])

  

  
  return table

table_100yr = data_parser(data_100yr)
table_2012 = data_parser(data_2012)

combined = zip(table_2012, table_100yr)

print"Month\tAverage\t\tHigh\t\tLow"

for i in combined[1:]:
  avg_diff = float(i[0][1]) / i[0][0] - i[1][1] / i[1][0]
  high_diff = i[0][2] - i[1][2]
  low_diff = i[0][3] - i[1][3]

  print("{}\t{:.1f} ({:.1f})\t{} ({})\t{} ({})".format(combined.index(i), float(i[0][1]) / i[0][0], avg_diff, i[0][2], high_diff, i[0][3], low_diff))

data_100yr.close()
data_2012.close()
