#!/usr/bin/env python3

# Define dictionaries
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
dictionary = {1: 'Hello', 2: 'World'}

# Access to items
print(student['name'])
print(dictionary[1])
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

# Update an item
student['phone'] = '555-5555'
print(student.get('phone'))

# Update items
student.update({'name': 'Jane', 'age': 26, 'phone': '777-7777'})
print(student)

# Remove an item
del student['phone']
print(student)

# Remove an item with pop() method
age = student.pop('age')
print(student)
print(age)

# Length of a Dictionary
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# Loop through Dictionary
for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
