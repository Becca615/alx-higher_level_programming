#!/usr/bin/python3
"""Function that creates a class MyList that inherits from list"""


class MyList(list):
    """subclass inheriting from another class or object"""
    def print_sorted(self):
        """Public instance method: def print_sorted(self): that prints
            the list, but sorted (ascending sort)"""
        print(sorted(self))
