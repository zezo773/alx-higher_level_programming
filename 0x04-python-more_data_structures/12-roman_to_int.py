#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (not isinstance(roman_string, str)):
        return 0

    romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    res = 0
    i = 0

    while i < len(roman_string):
        cur = romanMap[roman_string[i]]

        if i + 1 < len(roman_string):
            nxt = romanMap[roman_string[i + 1]]
            if cur < nxt:
                res += nxt - cur
                i += 2
                continue
        res += cur
        i += 1
    return res

