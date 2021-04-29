#!/usr/bin/python3
if __name__ == "__main__":
    # import the calculator file, to call all the functions
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    # print the result of each function
    print(a, '+', b, '=', add(a, b))
    print(a, '+', b, '=', sub(a, b))
    print(a, '+', b, '=', mul(a, b))
    print(a, '+', b, '=', div(a, b))