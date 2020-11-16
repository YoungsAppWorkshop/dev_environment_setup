#!/usr/bin/env python3


# Class: Blueprint for creating instances
class Employee:

    # Constructor
    def __init__(self, first, last, pay):
        # Python convention - first parameter for methods: self(instance arg)
        # Attributes - Instance Variables
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    # Method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# Instances
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.fullname())
