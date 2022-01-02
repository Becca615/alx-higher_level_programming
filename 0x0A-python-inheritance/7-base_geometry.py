#!/usr/bin/python3
"""class BaseGeometry."""


class BaseGeometry:
    """class BaseGeometry (based on 6-base_geometry.py)."""
    def area(self):
        """Public instance method:"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method:"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
