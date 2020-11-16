#!/usr/bin/env python3

# Tuples: an immutable data structure
# Lists are mutable and Tuples are immutable

# Creating an Empty Tuple
# empty_tuple = ()
# empty_tuple = tuple()

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# TypeError: 'tuple' object does not support item assignment
tuple_1[0] = 'Art'

print(tuple_1)
# print(tuple_2)
