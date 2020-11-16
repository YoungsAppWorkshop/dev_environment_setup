#!/usr/bin/env python3

"""
    Variable scope:               LEGB
    Local, Enclosing, Global, Built-in
"""

# Define a global variable
x = 'global x'


def test():
    """
    Example 1: Defining a local variable, and accessing to a global variable
    in a Function
    """

    # Define a local variable
    y = 'local y'
    print(y)

    # Trying to access to a global variable works fine
    print(x)


test()
# Trying to access to a local variable throws a NameError
# print(y)


def test2():
    """
    Example 2: If there's a local variable which has the same name with a
    global variable in a function, the global variable will be ignored
    in the function
    """

    # Define a local variable
    x = 'local x'

    # This line will print local x
    print(x)


test2()
print(x)


def test3():
    """
    Example 3: Using 'global' statement in a function allows to access
    into a global variable in a function
    """

    # Now x is pointing the global x variable
    global x
    x = 'This is global x'

    # This line will print local x
    print(x)


test3()
print(x)


# Parameter z is a local variable
def test4(z):
    """
    Example 4: Parameters are local variables
    """

    print(z)


test4('local z')

# Trying to access to a Parameter throws a NameError
# print(z)


"""
Example 5: Built in scope: Access to built-in function like min()
"""
m = min([5, 1, 4, 2, 3])
print(m)

# To see the list of all built in variables:
# import builtins
# print(dir(builtins))


# Be careful not to overwrite the built-in variables
# For example, the below code snippets will throw TypeError
#
# def min():
#     pass
#
#
# m = min([5, 1, 4, 2, 3])
# print(m)


def outer():
    """
    Example 6: Enclosing scope in nested functions

    Using 'nonlocal' statement allows to access
    into outer x variable
    """
    x = 'outer x'

    def inner():
        # nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
