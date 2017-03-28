"""With Demo

This program reads temperatures in fahrenheit from
a file, converts them to centigrade (in a function) and
creates a report file with the results.
It stops when the input is an empty string (end of file).
Also, there is an example of using the !r format character.
"""

def fahrenheit_to_centigrade(xtmp):
    nutmp = 5.0 /9.0 * (xtmp - 32)
    return nutmp

with open('/home/student/pydata/temps.dat') as filein,  \
     open('/home/student/pydata/temprpt.txt', 'w') as fileout:
#with open('c:/pydata/temps.dat') as filein,  \
#     open('c:/pydata/temprpt.txt', 'w') as fileout:
    for linein in filein:
        try:
            ftemp = float(linein)
        except ValueError:
            print('Input contains non-numeric data - {0!r}'.format(linein))
            continue
        ctemp = fahrenheit_to_centigrade(ftemp)
        tmp = '{0:.1f} degrees Fahrenheit is {0:.1f} degrees Centigrade\n'
        outline = tmp.format(ftemp, ctemp)
        fileout.write(outline)
