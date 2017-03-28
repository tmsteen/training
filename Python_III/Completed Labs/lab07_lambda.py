"""lab07_lambda.py

This program reads temperatures in fahrenheit from
the keyboard, converts them to centigrade (in a lambda function)
and prints the result.  This program also tests for a null entry

The test "if temp" returns false if the string entered is empty.
"""

nutmp = lambda tmp : 5.0 /9.0 * (tmp - 32)
while True:
    temp = input('Enter a temperature: ')
    if temp and (temp in 'qQ'):  # Ensure temp is not empty
        break
    try:
        ftemp = float(temp)
    except ValueError:
        print('Input contains non-numeric data - try again')
        continue
    ctemp = nutmp(ftemp)
    print('{:.1f} degrees Fahrenheit is {:.1f} degrees Centigrade'.format(
        ftemp, ctemp))


