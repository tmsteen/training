list = range(2, 18, 3)
list1 = []
list2 = []
sum = 0


for i in list:
  if i % 2 == 0:
     list1.append(i)
  list2.append(i*i)
  sum +=i

print list
print list1
print list2
print sum
