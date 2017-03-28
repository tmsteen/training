"""lab08_generator.py

Generator program returns even numbers or the word 'odd'.  This
program uses both methods of handling a generator: a for loop and
direct use of the next method and StopIteration detection.
"""

def gen2(start, end):
    
    for n in range(start, end + 1):
        if n % 2 == 1:
            result = "odd"
        else:
            result = n
        yield result

print("Calling generator")

for i in gen2(4, 15):
    print(i)
print()

x = gen2(4, 15)
print("What is x holding?")
print(x)
while True:
    try:
        print(next(x))
    except StopIteration:
        break
