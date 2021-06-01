#!/usr/bin/python3
"""module"""


class MyList(list):
    """
    Creating a class MyList that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))
