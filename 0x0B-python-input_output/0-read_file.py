#!/usr/bin/python3
"""text-file teadimg function definition"""


def read_file(filename=""):
    """contents of a UTF8 text file are printed to stdout"""
    with open(filename, encoding="utf - 8") as f:
        print(f.read(), end=" ")
