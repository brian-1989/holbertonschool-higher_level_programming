#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as ar
    from calculator_1 import add, sub, mul, div
    length_argv = len(ar) - 1
    num_1 = 0
    num_2 = 0
    if length_argv != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif ar[2] != "+" and ar[2] != "-" and ar[2] != "*" and ar[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        num_1 = int(ar[1])
        num_2 = int(ar[3])
        if ar[2] == "+":
            print("{} + {} = {}".format(num_1, num_2, add(num_1, num_2)))
        elif ar[2] == "-":
            print("{} - {} = {}".format(num_1, num_2, sub(num_1, num_2)))
        elif ar[2] == "*":
            print("{} * {} = {}".format(num_1, num_2, mul(num_1, num_2)))
        else:
            print("{} / {} = {:d}".format(num_1, num_2, div(num_1, num_2)))
