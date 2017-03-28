#!/usr/bin/python3

temp_list = [(f, 5.0/9.0 * (f - 32)) for f in range(-40, 120, 10) if f != 0 and f != 50]
print("This is a list...")
print(temp_list)
print()

temp_set = {(f, 5.0/9.0 * (f - 32)) for f in range(-40, 120, 10) if f != 0 and f != 50}
print("This is a set...")
#print(temp_set)
[print("{}, {:.2f}".format(x[0], x[1])) for x in temp_set]
print()

temp_dict = {f: 5.0/9.0 * (f - 32) for f in range(-40, 120, 10) if f != 0 and f != 50}
print("This is a dictionary...")
print(temp_dict)
print()
