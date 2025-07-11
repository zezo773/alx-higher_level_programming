#!/usr/bin/python3

class Square:

    """A class that defines a square by its size"""
    def __init__(self, size=0, position=(0, 0)):
            self.size = size
            self.position = position
    def area(self):
        """Method that returns the square are of the object"""
        return (self.__size ** 2)
    @property
    def size(self):
        """Method to returns the size value"""
        return self.__size
    @size.setter
    def size(self, value):
        """Method to set the size value of the square object"""
        if not isinstance(value, int):
            raise TypeError("size must be an intger")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if (self.__size == 0):
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
