#!/usr/bin/env python3
def add_numbers(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)


add_numbers(3)
add_numbers(3, 2)
add_numbers(1, 3, 5, 6, 7, 8)
