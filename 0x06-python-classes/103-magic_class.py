#!/usr/bin/python3
"""magic class defin"""
import math


class MagicClass:
    """initialize a magic class"""

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """area func"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """circ func"""
        return (2 * math.pi) * self.__radius
