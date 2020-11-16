#!/usr/bin/env python3

# Creating an Empty List
# empty_list = []
# empty_list = list()

# Create a List
courses = ['History', 'Math', 'Physics', 'CompSci']

# Length of a List
print(len(courses))

# Access to items of a List
print(courses[0])
print(courses[-1])

# Access to the first 2 items of the List
print(courses[0:2])

# Slice the list
print(courses[:2])
print(courses[2:])

# List methods for appending, removing items
courses.append('Art')
print(courses)

courses.insert(1, 'English')
print(courses)

courses_1 = ['Korean', 'Geology']
courses.extend(courses_1)
print(courses)

courses.remove('Math')
print(courses)

popped = courses.pop()
print(courses)
print(popped)

# List methods for sorting the List
courses.reverse()
print(courses)

# List.sort() modifies the original list
# courses.sort()
# print(courses)

# Sorted function doesn't modify the original list
sorted_courses = sorted(courses, reverse=True)
print('Original List', courses)
print('Sorted List', sorted_courses)

nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

# Methods for the List containing numbers
print(max(nums))
print(min(nums))
print(sum(nums))

# Get the index of an item of the List
print(courses.index('Physics'))
print('Math' in courses)

# Looping through Lists
for item in courses:
    print(item)

for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)

# Joining a List into a String
course_str = ', '.join(courses)
print(course_str)

# Splitting a String to a List
new_list = course_str.split(', ')
print(new_list)
