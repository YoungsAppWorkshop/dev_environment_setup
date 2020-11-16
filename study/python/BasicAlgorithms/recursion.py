#!/usr/bin/env python3
"""
Recursion

    Instruction:

        Implement a function recursivly to get the desired
        Fibonacci sequence value.
        Your code should have the same input/output as the
        iterative code in the instructions.

"""


def recursive_example(input):
    """ Simple Recursive Function """
    if input <= 0:
        return input
    else:
        output = recursive_example(input - 1)
        return output


def fib(position):
    """ Fibonacci sequence function using for loop"""
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        first, second = 0, 1
        next = first + second
        for index in range(2, position):
            first = second
            second = next
            next = first + second
        return next


def fib_recursive(position):
    """ Fibonacci sequence function using recursive algorithm"""
    if position < 0:
        return -1
    elif position == 0 or position == 1:
        return position
    else:
        return fib_recursive(position - 2) + fib_recursive(position - 1)


if __name__ == '__main__':
    print(fib(5))
