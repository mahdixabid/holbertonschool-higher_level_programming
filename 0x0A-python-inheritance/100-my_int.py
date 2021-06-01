#!/usr/bin/python3
"""
class module
"""


class MyInt(int):
    """class with int object"""

    def __eq__(self, other):
        """equal equal method"""
        return int(self) != int(other)

    def __ne__(self, other):
        """not equal method"""
        return int(self) == int(other)
