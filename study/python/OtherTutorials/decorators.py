#!/usr/bin/env python3


# Closure
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function


# Decorator Function
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(original_function.__name__))  # noqa
        return original_function(*args, **kwargs)
    return wrapper_function


# Decorator Class
class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))  # noqa
        return self.original_function(*args, **kwargs)


# display = decorator_function(display)
@decorator_function
def display():
    print('display function ran')


# display_info = decorator_function(display_info)
@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


@decorator_class
def test():
    print('test function ran')


display()
display_info('John', 25)
test()
