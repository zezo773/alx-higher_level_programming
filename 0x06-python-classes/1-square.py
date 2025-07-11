#!/usr/bin/python3
"""Define a Square class."""

class Square:
    """Class that defines a square.

    Attribute:
        __size : the size of the square (privat)
    """
    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the square.
        """
        self.__size = size
