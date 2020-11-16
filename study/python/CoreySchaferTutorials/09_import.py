#!/usr/bin/env python3

# import my_module
# import my_module as m
# from my_module import *
# from my_module import find_index as fi, test
from my_module import find_index, test
import sys
import random
import math

# Python automatically checks multiple locations to find a my_module
# To find out which location Python checks, import sys, and print sys.path
# print(sys.path)

# Locations can be added into sys.path
# sys.path.append('/Users/Young/Desktop/temp')

# Setting Python Path environment variable in .bash_profile
# export PYTHONPATH="/Users/Young/Desktop/temp"

courses = ['History', 'Math', 'Physics', 'Art']

# index = my_module.find_index(courses, 'Math')
# index = m.find_index(courses, 'Math')
# index = fi(courses, 'Math')
# index = find_index(courses, 'Math')
#
# print(index)
# print(test)

# Standard Library examples
random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)

# Find out Standard Library modules locations
print(math.__file__)
