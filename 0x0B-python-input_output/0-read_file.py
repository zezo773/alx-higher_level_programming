#!/usr/bin/python3
""" a function that reads a text file """

def read_file(filename=""):
    """
    a function that reads a text file
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
