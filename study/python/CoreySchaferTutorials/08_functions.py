#!/usr/bin/env python3


# Function definition and pass statement
def func_01():
    pass


# Print Function
print(func_01)

# Execute Function
print(func_01())
func_01()


# Parameters: local scope
# Function with a Default Value
def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


print(hello_func('Hi', name='Corey'))


# *args, **kwargs
# args:         arguments
# kwargs:       keyword arguments
def student_info(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)

# student_info('Math', 'Art', name='John', age=22)
student_info(*courses, **info)
