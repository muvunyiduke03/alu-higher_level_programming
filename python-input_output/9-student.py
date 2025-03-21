#!/usr/bin/python3
"""
Module: 9-student
Defines a class Student with public attributes and a method
to retrieve a dictionary representation of the object.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: The dictionary representation of the instance.
        """
        return self.__dict__
