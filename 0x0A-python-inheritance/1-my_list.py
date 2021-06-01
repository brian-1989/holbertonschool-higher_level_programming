#!/usr/bin/python3
"""
class Mylist
"""


class MyList(list):
    """class that inherits a list.

    """
    def print_sorted(self):
        """method that print a list in ascending order.

        """
        print(sorted(self))
