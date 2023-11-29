#!/usr/bin/python3
"""This module defines a function to print a person's name."""

def say_my_name(first_name, last_name=""):
    """
    Print the first and last name.

    Args:
    first_name (str): The first name of the person.
    last_name (str, optional): The last name of the person. Defaults to "".

    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
