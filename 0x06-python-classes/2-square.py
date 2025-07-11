#!/usr/bin/python3

class Square:
    """Class that defines a square by its size.

    Attributes:
        __size: the size of the square
    """

    def __init__(self, size=0):
        """Initialize a square instance
        Args:
            size: the size of square
        Raises:
            TypeError: if size is not an intger
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an intger")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
