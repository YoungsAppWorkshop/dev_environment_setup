#!/usr/bin/env python3

"""
    Sorting List Example 1
"""
# Get a sorted copy of a List
my_list = [9, 1, 8, 2, 7, 6, 3, 5, 4, 0]
sorted_list = sorted(my_list)

print('Original List: ', my_list)
print('Sorted List: ', sorted_list)

# Sort the original List
my_list.sort()
print('Original List (sorted): ', my_list)

# Sort a List in descending order
sorted_list = sorted(my_list, reverse=True)
my_list.sort(reverse=True)

print('Original List (reverse=True): ', my_list)
print('Sorted List (reverse=True): ', sorted_list)


"""
    Sorting Tuple Example
"""
my_tuple = (9, 1, 8, 2, 7, 6, 3, 5, 4, 0)

# Tuple is immutable
# Tuple doesn't have sort() method

# The below line throws AttributeError
# my_tuple.sort()

sorted_tuple = tuple(sorted(my_tuple))
print('Sorted Tuple: ', sorted_tuple)


"""
    Sorting Dictionary Example
"""
my_dict = {'name': 'Young', 'os': 'Mac', 'job': 'developer', 'gender': 'male'}

# The below line will sort the keys of the dictionary
sorted_dict = sorted(my_dict)

print('Sorted Dictionary Keys: ', type(sorted_dict), sorted_dict)


"""
    Sorting with Keys Example 1
        - Sorting with Absolute values
"""
nums = [-4, -5, -6, 1, 3, 2]
sorted_nums = sorted(nums)
sorted_abs = sorted(nums, key=abs)

print('Original Numbers: ', nums)
print('Sorted Numbers: ', sorted_nums)
print('Sorted Absolute Values: ', sorted_abs)


"""
    Sorting with Keys Example 2
        - Sorting with an Attribute of objects
"""


class Employee():
    """ Class representing an Employee """

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


def e_sort(emp):
    return emp.name


e1 = Employee('Kim', 28, 50000)
e2 = Employee('Joung', 34, 65000)
e3 = Employee('Young', 39, 60000)

employees = [e1, e2, e3]
# The below line throws TypeError
# sorted_employees = sorted(employees)

# key should be specified to sort objects
sorted_employees = sorted(employees, key=e_sort)

# Using a Lambda function
# sorted_employees = sorted(employees, key=lambda e: e.name)

# Using operator module
# from operator import attrgetter
# sorted_employees = sorted(employees, key=attrgetter('salary'))

# Sorting in descending order
# sorted_employees = sorted(employees, key=e_sort, reverse=True)

print('Sorted Employees List: ', sorted_employees)
