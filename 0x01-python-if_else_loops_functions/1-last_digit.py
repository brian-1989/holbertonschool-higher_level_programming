#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "and is less than 6 and not 0"
# condition to when number is positive or negative
if number > 0:
    # l_d = last digit
    L_d = number % 10
else:
    L_d = number % - 10
# conditions to the last digit
if L_d < 6 and L_d != 0:
    print("Last digit of {} is {} {}".format(number, L_d, string))
elif Last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, L_d))
else:
    print("Last digit of {} is {} and is greater than 5".format(number, L_d))
