#!/usr/bin/python3
"""Class Student that defines a student"""


class Student:
    """Contains Student data"""

    def __init__(self, first_name, last_name, age):
        """Student initialization
            Args:
                first_name (str): Student's first name.
                last_name (str): Student's last name.
                age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary"""

        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            temp_list = {}
            for element in attrs:
                if type(element) is not str:
                    return self.__dict__
                if element in self.__dict__.keys():
                    temp_list[element] = self.__dict__[element]
            return temp_list

    def reload_from_json(self, json):
        """Replace all Student attributes on JSON"""

        for items in json.keys():
            self.__dict__[items] = json[items]
