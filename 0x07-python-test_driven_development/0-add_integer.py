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
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or float, and b must be an integer or float")
    a = int(a)
    b = int(b)
    return a + b
