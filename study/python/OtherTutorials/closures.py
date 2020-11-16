#!/usr/bin/env python3


# def outer_func(msg):
#     message = msg
#
#     def inner_func():
#         print(message)
#
#     return inner_func
#
#
# hi_func = outer_func('hi')
# hello_func = outer_func('hello')
#
# hi_func()
# hello_func()


import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))  # noqa
        print(func(*args))
    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(3, 2)
sub_logger(4, 5)
