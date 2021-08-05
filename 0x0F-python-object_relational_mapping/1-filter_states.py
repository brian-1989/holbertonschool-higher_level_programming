#!/usr/bin/python3
""" Connect a file .py with an data base.

"""


import MySQLdb
from sys import argv


def data_base():
    """ Function to connect a file python with an data base and print an query.

    """
    my_dd = MySQLdb.connect(host="localhost",
                            user=argv[1],
                            passwd="Brian1995#",
                            db=argv[3],
                            port=3306)
    my_cursor = my_dd.cursor()
    my_cursor.execute("SELECT id, name FROM states WHERE name like 'N%'")
    data = my_cursor.fetchone()
    while data:
        print(data)
        data = my_cursor.fetchone()
    my_dd.close()


if __name__ == '__main__':
    """ When it imported the file not be executed.

    """
    data_base()
