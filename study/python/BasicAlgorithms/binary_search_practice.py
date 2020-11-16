#!/usr/bin/env python
"""
Binary Search

    Instruction:
        You're going to write a binary search function.
        You should use an iterative approach - meaning
        using loops.

        Your function should take two inputs:
        a Python list to search through, and the value
        you're searching for.

        Assume the list only has distinct elements,
        meaning there are no repeated values, and
        elements are in a strictly increasing order.

        Return the index of value, or -1 if the value
        doesn't exist in the list.

    Efficiency:
        O(log(n))

    Visualization of Binary Search:
        https://www.cs.usfca.edu/~galles/visualization/Search.html
"""


def binary_search(input_array, value):
    """ Simple Binary Search Function """

    first = 0
    last = len(input_array) - 1

    while first <= last:
        i = (first + last) / 2

        print 'comparing array[{i}] element {element} with {value}'.format(
            i=i, element=input_array[i], value=value)
        if input_array[i] == value:
            return '{value} found at position {i}'.format(value=value, i=i)
        elif input_array[i] > value:
            last = i - 1
        elif input_array[i] < value:
            first = i + 1
    return -1


if __name__ == '__main__':
    test_list = [1, 3, 9, 11, 15, 19, 29, 30]
    print binary_search(test_list, 29)

    test_list = [1, 3, 9, 11, 15, 19, 29, 30, 31]
    print binary_search(test_list, 3)
