#!/usr/bin/python3
"""
Student.
"""


class Student:
    """class that defines a student.

    """
    def __init__(self, first_name, last_name, age):
        """initial method that take the arguments.
        Args:
             first_name: name of student
             last_name: last name of student
             age: age of student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that convert the self in a diccionary.
        Return the retrieves a dictionary representation of a Student

        """
        return self.__dict__
