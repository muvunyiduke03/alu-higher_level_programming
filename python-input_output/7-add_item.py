#!/usr/bin/python3
"""
Module: 7-add_item
Adds all command-line arguments to a Python list and saves them to a file.

The list is stored in a JSON file called add_item.json. If the file
does not exist, it is created. If it exists, the arguments are appended
to the existing list and then saved back to the file.

Dependencies:
- save_to_json_file from 5-save_to_json_file.py
- load_from_json_file from 6-load_from_json_file.py
"""


import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"


if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []


items.extend(sys.argv[1:])


save_to_json_file(items, filename)