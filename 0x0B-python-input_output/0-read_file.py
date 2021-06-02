#!/usr/bin/python3
"""module"""


def read_file(filename=""):
    """read a file"""

    with open(filename, encoding="utf-8") as f:
        for paragraph in f.read():
            print(paragraph, end="")
