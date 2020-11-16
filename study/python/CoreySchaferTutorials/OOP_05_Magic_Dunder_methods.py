#!/usr/bin/env python3


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    """
        __repr__
            - Unambiguous representation of an object
            - Logging/Debugging for Develpers
    """

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first,
                                                   self.last,
                                                   self.pay)

    """
        __str__
            - Readable representation of an object
            - Display to the end-users
    """

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # More examples for Dunder methods
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


# Instances
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(repr(emp_1))
print(str(emp_1))

# The below line will print emp_1.__str__ first, if __str__ isn't defined,
# it'll print emp_1.__repr__
print(emp_1)

print(emp_1 + emp_2)

"""
    Dunder method example
"""
print(1 + 2)
print(int.__add__(1, 2))

print('a' + 'b')
print(str.__add__('a', 'b'))
