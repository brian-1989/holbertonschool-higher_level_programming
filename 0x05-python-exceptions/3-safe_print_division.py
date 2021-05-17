#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        _div = a / b
    except ZeroDivisionError:
        # It is assigned to the variable _div, the value of none
        _div = None
    finally:
        print("Inside result: {}".format(_div))
    return _div
