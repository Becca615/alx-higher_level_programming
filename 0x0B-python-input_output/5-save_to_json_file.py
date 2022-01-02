#!/usr/bin/python3
"""
function that writes an Object to a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    You must use the with statement
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
