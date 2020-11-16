#!/usr/bin/env python3

nums = [1, 2, 3, 4, 5]

# Break and Continue statements
print('Break statement')
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

print('\nContinue statement')
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

# Nested Loops
for num in nums:
    for letter in 'abc':
        print(num, letter)

# Looping with index
for index in range(10):
    print(index)

for index in range(1, 11):
    print(index)
