#!/usr/bin/python3

""" from_json_string module """
import json

def from_json_string(my_str):
    """
    Return a JSON object
    """
    try:
        return json.loads(my_str)
    except json.JSONDecodeError as e:
        raise ValueError(str(e))
