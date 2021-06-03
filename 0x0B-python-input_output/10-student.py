#!/usr/bin/python3
"""
Class Student.
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

    def to_json(self, attrs=None):
        """method that adds in a dictionary existing attributes.
        Return the dictionary with the attributes.

        """
        my_dic = {}
        if attrs is None:
            my_dic['firs_name'] = self.first_name
            my_dic['last_name'] = self.last_name
            my_dic['age'] = self.age
            return my_dic
        if type(attrs) is list:
            for i in attrs:
                if i is 'first_name':
                    my_dic[i] = self.first_name
                if i is 'last_name':
                    my_dic[i] = self.last_name
                if i is 'age':
                    my_dic[i] = self.age
            return my_dic
