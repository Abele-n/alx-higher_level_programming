#!/usr/bin/python3
"""file-appending function definition"""


def append_write(filename="", text=""):
    """Adds a string to the end of the UTF8 text file

    Args:
    filename(str): name of filename to append to
    Returns:
    the number of appended characters
    """

    with open(filename, "a", encoding="utf -8") as f:
        return f.write(text)
