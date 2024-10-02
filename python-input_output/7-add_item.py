#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a file using a JSON representation.
"""

import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

"""
Check if the file exists. If it does, load the existing list from the file.
Otherwise, initialize an empty list.
"""
if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Extend the list by adding all the command-line arguments
# (except the script name).
# These are passed as additional items to be appended to the list.
items.extend(sys.argv[1:])

# Save the updated list back to the file in
# JSON format using the save_to_json_file function.
save_to_json_file(items, filename)
