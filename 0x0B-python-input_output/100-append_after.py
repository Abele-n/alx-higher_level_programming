#!/usr/bin/python3
"""text file insertion function definition"""


def append_after(filename="", search_string="", new_string=""):
    """A new text is inserted after each line having a given string

    Args:
    filename(str): name of the file
    new_string: string to insert
    search string: string to search for within the file
    """

    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
