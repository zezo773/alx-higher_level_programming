#!/usr/bin/python3
""" a function that writes a string to a text file """

def write_file(filename="", text=""):
    """
    a function that writes a string to a text file
    """

    with open(filename, "w", encoding="UTF-8") as f:
        return (f.write(text))
