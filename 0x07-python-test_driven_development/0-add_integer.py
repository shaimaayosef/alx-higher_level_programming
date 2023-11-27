#!/usr/bin/python3
"""This module provides a function to add two numbers."""

def add_integer(a, b=98):
    """Add two numbers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b, casted to an integer.

    Raises:
        TypeError: If a or b is not an integer or float.

    Example:
        >>> add_integer(3, 5)
        8
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
