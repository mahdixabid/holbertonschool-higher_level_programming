#!/usr/bin/python3
""" this class define a Rectangle"""


class Rectangle:
        """Represent a Rectangle."""

        def __init__(self, width=0, height=0):
                """Initializer object with width and height values."""

                self.width = width
                self.height = height

        @property
        def width(self):
                """Convert the atribute width to a atribute
                editable with self.width
                """
                return self.__width

        @width.setter
        def width(self, value):
                """Assined te value to width with the variable value"""

                if not isinstance(value, int):
                        raise TypeError("width must be an integer")
                if value < 0:
                        raise ValueError("width must be >= 0")
                self.__width = value

        @property
        def height(self):
                """Convert the atribute height to the attribute
                editable with self.height
                """

                return self.__height

        @height.setter
        def height(self, value):
                """Assinded the value to self.height with variable value"""

                if not isinstance(value, int):
                        raise TypeError("height must be an integer")
                if value < 0:
                        raise ValueError("height must be >= 0")
                self.__height = value

        def area(self):
                """Return the area of the rectangle"""

                return (self.__width * self.__height)

        def perimeter(self):
                """return perimeter of the rectangle"""

                if self.__width == 0 or self.__height == 0:
                        return 0
                return ((self.__width * 2) + (self.__height * 2))
