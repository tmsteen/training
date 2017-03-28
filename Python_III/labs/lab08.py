#!/bin/python3

def gen(start, stop):
    for i in range(start, stop + 1):
        if i % 2 == 1:
            result = "odd"
        else:
            result = i
        
        yield result
        
for i in gen(4,15):
    print(i)
