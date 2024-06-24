#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    my_set = set(my_list)
    sums = sum(my_set)
    return sums
