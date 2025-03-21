#!/usr/bin/python3
"""
This module defines the Student class, which implements serialization
and deserialization mechanisms for representing and rebuilding a student
object in JSON format.
"""


class Student:
    """
    A class that defines a student with specific attributes and methods
    for JSON serialization and deserialization.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the instance,
                  filtered by attrs if provided.
        """

        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {
                key: getattr(self, key) for key in attrs
                if hasattr(self, key)
                }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with those
        from a JSON dictionary.

        Args:
            json (dict): A dictionary containing the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
