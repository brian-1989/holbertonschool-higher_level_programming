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
    my_cursor.execute("SELECT cities.name FROM cities INNER JOIN states\
        ON cities.state_id = states.id WHERE states.name=%s\
        ORDER BY cities.id ASC", (argv[4], ))
    data = my_cursor.fetchone()
    while data:
        print("{}".format(data[0]), end="")
        data = my_cursor.fetchone()
        if data is None:
            break
        print(", ", end="")

    print(end="\n")
    my_db.close()


if __name__ == '__main__':
    """ When it imported the file not be executed.

    """
    data_base()
