#!/usr/bin/env python3

# Define a string variable
message = 'Bobby\'s World'

# Print a string variable
print(message)

# Length of message
print(len(message))

# Print the first character of a string
print(message[0])

# Print the first 5 characters of a string
print(message[0:5])
print(message[:5])

# Slicing a string variable
print(message[6:])

# String methods
print(message.lower())
print(message.count('B'))

# Replace string
message = 'Hello World'
new_message = message.replace('World', 'Universe')
print(message)
print(new_message)

# Concatenate String
greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'
print(message)

# Formatted string
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# F string - python 3.6 and above
# message = f'{greeting}, {name}. Welcome!'
# print(message)

# dir() method: Show all methods and attributes for a class
print(dir(message))
print(help(str))
print(help(str.lower))
