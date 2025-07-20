#!/usr/bin/python3

class Node:
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    @property
    def next_node(self):
        return self.__next_node
