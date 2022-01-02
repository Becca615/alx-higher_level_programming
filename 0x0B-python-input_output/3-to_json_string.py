#!/usr/bin/python3
"""
function that returns the JSON
representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """
    You t need to manage exceptions if the object t be serialized.
    """
    return(json.dumps(my_obj, sort_keys=True))
