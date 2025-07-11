#!/usr/bin/python3

class Square:

    """
    Represents a square.

    Attributes:
        __size: the length of the square's side
    """

    def __init__(self, size=0):
        
        """
        Intializes a new square instance.

        Args:
            size: the length of the square side

        Raise:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an intger")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: the area of the square
        """
        return self.__size ** 2
