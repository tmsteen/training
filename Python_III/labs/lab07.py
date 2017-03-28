"""
This program reads a temperature in fahrenheit from
the keyboard, converts it to centigrade (in a function) and prints the
results. Then it requests another input from the keyboard.
"""

f_to_c = lambda xtmp : 5.0 / 9.0 * (xtmp - 32)

while True:
    temp = input('Enter a temperature: ')
    if temp == 'q' or temp == 'Q':  
        break
    try:
        ftemp = float(temp)
    except ValueError:
        print('Input contains non-numeric data - try again')
        continue
    ctemp = f_to_c(ftemp)
    print('{:.1f} degrees Fahrenheit is {:.1f} degrees Centigrade'.format(
        ftemp, ctemp))
