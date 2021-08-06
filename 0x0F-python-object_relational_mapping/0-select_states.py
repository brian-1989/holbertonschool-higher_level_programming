#!/usr/bin/python3
""" Connect a file .py with an data base.

"""


import MySQLdb
from sys import argv


def data_base():
    """ Function to connect a file python with an data base and print an query.

    """
    my_db = MySQLdb.connect(user=argv[1],
                            passwd="Brian1995#",
                            db=argv[3])
    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    data = my_cursor.fetchone()
    while data:
        print(data)
        data = my_cursor.fetchone()
    my_db.close()


if __name__ == '__main__':
    """ When it imported the file not be executed.

    """
    data_base()
