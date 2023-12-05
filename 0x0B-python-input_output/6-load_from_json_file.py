#!/usr/bin/python3
"""load from json"""
import json

def load_from_json_file(filename):
    """load from json to file"""
    try:
        with open(filename, encoding="utf-8") as file_loaded:
            return json.load(file_loaded)
    except FileNotFoundError as e:
        print("[{}] {}".format(e.__class__.__name__, e))
        return None
    except ValueError as e:
        print("[{}] {}".format(e.__class__.__name__, e))
        return None
