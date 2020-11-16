#!/usr/bin/env python3

# Creating an Empty Set
# empty_set = {}  # This isn't right! It's a dictionary
# empty_set = set()

# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)

# Sets methods
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
print(cs_courses)
