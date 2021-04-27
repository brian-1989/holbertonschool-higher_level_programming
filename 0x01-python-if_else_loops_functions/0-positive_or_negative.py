#!/usr/bin/python3
import random
'#random number'
number = random.randint(-10, 10)
'#condicitions to know if the number is positive, negative or zero'
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
