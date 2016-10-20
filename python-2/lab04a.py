#Stack

stack = []

for i in range (0,5):
  stack.append(i)
  print("Stack: " + str(stack))
  
while len(stack) > 0:
  value = stack.pop()
  print("Stack: " + str(stack) + " Popped: " + str(value))

for i in range (0,5):
  stack.insert(0,i)
  print("Stack: " + str(stack))
  
while len(stack) > 0:
  value = stack.pop()
  print("Stack: " + str(stack) + " Popped: " + str(value))

