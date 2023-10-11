#!/usr/bin/python3
"""file-writing function definition"""


def write_file(filename="", text=""):
    """convert a string to a UTF8 text file

    Args:
    text(str): the text to write to a file
    filename(str): name of file to write
    Return:
    the witten number of characters
    """

    with open(filename, "w", encoding="utf - 8") as f:
        return f.write(text)
