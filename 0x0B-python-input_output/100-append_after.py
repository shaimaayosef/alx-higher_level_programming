#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """class body."""
    text = ""
    with open(filename) as r:
        for line in r:
            # Remove 'Holberton' from each line
            line_without_holberton = line.replace('Holberton', '')
            text += line_without_holberton

            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
