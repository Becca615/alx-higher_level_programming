#!/usr/bin/python3
"""class Square."""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return(self.__size ** 2)

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__size, self.__size))
