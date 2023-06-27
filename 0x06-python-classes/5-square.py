#!/usr/bin/python3
""" define class Square """


class Square:
    """ initialize a square class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size **2

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            i = 1
            while(i <= self.__size):
                print("#" * self.__size)
                i+= 1
