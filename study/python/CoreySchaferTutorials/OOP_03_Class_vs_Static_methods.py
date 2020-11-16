#!/usr/bin/env python3
import datetime


class Employee:
    # Class Variable
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # Instance Variables (Attributes)
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1

    # Instance Methods: Receive instance as the first argument automatically
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)

        # Using self intead of Employee for accessing to class variables
        # gives us ability to override class variables
        self.pay = int(self.pay * self.raise_amount)

    # Class Methods: Receive class as the first argument automatically
    @classmethod
    def set_raise_amount(cls, amount):
        # Python convention - first parameter for class methods: cls
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    # Static Methods: Receive no argument automatically
    # Static Methods logically related with the class, but it's similar to
    # regular functions
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Instances
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# Calling class method
Employee.set_raise_amount(1.05)
# Below line works, but it's not the best practice
# emp_1.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-King-45000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fullname())
print(new_emp_1.email)

# Calling static method
my_date = datetime.date(2017, 2, 13)
print(Employee.is_workday(my_date))
