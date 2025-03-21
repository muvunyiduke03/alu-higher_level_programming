#!/usr/bin/python3
"""
Module: 6-load_from_json_file
Defines a function that creates an object from a JSON file.
"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file containing the JSON representation.

    Returns:
        object: The Python data structure represented by the JSON file.
    """
    import json
    with open(filenamr, "r", encoding="utf-8") as f:
        return json.load(f)
