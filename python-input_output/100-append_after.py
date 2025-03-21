#!/usr/bin/python3
"""
This module provides a function to manipulate files by adding a specific
line of text after every line containing a given string.
The function makes use of the `with` statement for safe and concise file handling.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line containing the search_string.

    Example Usage:
        append_after("example.txt", "Python", "C is fun!\n")
    """

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
