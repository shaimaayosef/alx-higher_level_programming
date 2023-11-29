#!/usr/bin/python3
"""This module defines a function to print a square of 'x' characters with a given size."""

def print_square(size):
    """
    Print a square of 'x' characters with the given size.

    Args:
    size (int): The size of the square.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        print("x" * size)
