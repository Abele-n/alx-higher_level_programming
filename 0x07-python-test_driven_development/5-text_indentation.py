#!/usr/bin/python3
"""Defining a text indentation function"""


def text_indentation(text):
    """prints text followed by 2 new lines after '.', '?' and ':'

    Args:
    text(string): string text to print
    Raises:
    TypeError: if the text is not a string
    """

    d = 0
    while d < len(text) and text[d] == '':
        d +=1
        while c < len(text):
            print(text[d], end="")

