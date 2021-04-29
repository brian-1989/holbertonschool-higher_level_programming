#!/usr/bin/python3
if __name__ == "__main__":
    # import the calculator file, to call all the functions
    import calculator_1
    a = 10
    b = 5
    # print the result of each function
    print(a, '+', b, '=', calculator_1.add(a, b))
    print(a, '+', b, '=', calculator_1.sub(a, b))
    print(a, '+', b, '=', calculator_1.mul(a, b))
    print(a, '+', b, '=', calculator_1.div(a, b))