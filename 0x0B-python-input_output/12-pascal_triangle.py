#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        current_row = []
        for r in range(i+1):
            ncr = factorial(i) // (factorial(r) * factorial(i-r))
            current_row.append(ncr)
        triangle.append(current_row)

    return (triangle)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return (n * factorial(n - 1))
