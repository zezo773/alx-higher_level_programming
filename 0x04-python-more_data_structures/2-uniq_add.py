#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = set(my_list)
    total = 0
    for i in num:
        total += i
    return total
