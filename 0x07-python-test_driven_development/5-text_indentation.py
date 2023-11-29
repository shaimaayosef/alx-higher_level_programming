#!/usr/bin/python3
"""This module defines a function to indent text based on specific delimiters."""



def text_indentation(text):
    """
    Indent the text based on specific delimiters.

    Args:
    text (str): The text to be indented.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        words = (delimeter + "\n\n").join(
                [index.strip(" ") for index in words.split(delimeter)])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
