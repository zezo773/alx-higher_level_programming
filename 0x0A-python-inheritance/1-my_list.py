#!/usr/bin/python3
"""
a class MyList that inherits from list
"""
class MyList(list):
    """
    Subclass inhrit from list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
