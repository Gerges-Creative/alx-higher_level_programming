#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
'''
If the number is positive the last digit will be
positive, if the number is negative the last digit
will be negative so I have to time it by -1
'''

if number < 0:
    last_digit = number % -10
    if last_digit < 0:
        print(f'Last digit of {number} is {last_digit} and is less than 6 \
and not 0')
    else:
        print(f'Last digit of {number} is {last_digit} and is 0')
elif number > 0:
    last_digit = number % 10
    if last_digit > 5:
        print(f'Last digit of {number} is {last_digit} and is greater than 5')
    elif last_digit <= 5 and last_digit != 0:
        print(f'Last digit of {number} is {last_digit} and is less than 6 and\
 not 0')
    else:
        print(f'Last digit of {number} is {last_digit} and is 0')
else:
    print(f'Last digit of {number} is {last_digit} and is 0')
