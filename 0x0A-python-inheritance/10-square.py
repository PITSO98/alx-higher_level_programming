#!/usr/bin/python3
"""
module for square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inheret rectangle class
    """

    def __init__(self, size):
        """
        public instantiation
        """
        self.__size = size
        self.__width = size
        self.__height = size
        super().__init__(size, size)

    def __str__(self):
        """
        instance method to determine area of square
        """
        return ("[Rectangle] {:d}/{:d}".
                format(self.__class__.__name__,
                       self.__width,
                       self.__height))
