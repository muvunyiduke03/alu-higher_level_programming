#!/usr/bin/python3
"""
Module: 10-student
Defines a class Student with public attributes and a method
to retrieve a dictionary representation of the object, with optional filtering.
"""


class Student:
    """
    Defines a student by:
    - Public instance attributes: first_name, last_name, and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only the attributes in this list
        are retrieved. Otherwise, all attributes are retrieved.

        Args:
            attrs (list): Optional list of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the instance.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {
                attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)
                }
        return self.__dict__
