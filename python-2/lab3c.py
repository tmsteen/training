trees = open('/home/student/Python II Data/trees.dat')
tree_list = []
length = 0

for data in trees:
  tree_list.append(int(data))
  length += 1

tree_count = length
total_height = sum(tree_list)
average_height = float(total_height) / tree_count
tallest = max(tree_list)
shortest = min(tree_list)

print("Number of trees: " + str(tree_count))
print("Average height: {:.2f}".format(average_height))
print("Tallest tree: " + str(tallest))
print("Shortest tree: " + str(shortest))

