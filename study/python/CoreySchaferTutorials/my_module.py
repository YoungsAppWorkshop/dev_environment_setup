#!/usr/bin/env python3

print('Imported my_module.py')

test = 'Test String'


def find_index(to_search, target):
    """Find the index of a value in a sequence"""

    for index, value in enumerate(to_search):
        if value == target:
            return index

    return -1
