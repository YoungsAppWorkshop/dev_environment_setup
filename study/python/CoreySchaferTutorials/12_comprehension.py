#!/usr/bin/env python3

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


"""
    Example 1. List comprehension using For loop 1

    Basic Use case
"""
# my_list = []
# for num in nums:
#     my_list.append(num)
my_list = [num for num in nums]
print('Example 1: ', my_list)


"""
    Example 2. List comprehension using For loop 2

    Mapping items with List comprehension
"""
# my_list = []
# for num in nums:
#     my_list.append(num * num)
my_list = [num * num for num in nums]
print('Example 2: ', my_list)

# Using a map and lambda
# my_list = map(lambda num: num * num, nums)
# print(list(my_list))


"""
    Example 3. List comprehension using For loop 3

    Filtering items with List comprehension
"""
# my_list = []
# for num in nums:
#     if num % 2 == 0:
#         my_list.append(num)
my_list = [num for num in nums if num % 2 == 0]
print('Example 3: ', my_list)

# Using a filter and lambda
# my_list = filter(lambda num: num % 2 == 0, nums)
# print(list(my_list))


"""
    Example 4. List comprehension using For loop 4

    Nested For loop
"""
str1 = 'abc'
# my_list = []
# for letter in str1:
#     for num in range(len(str1)):
#         my_list.append((letter, num))
my_list = [(letter, num) for letter in str1 for num in range(len(str1))]
print('Example 4: ', my_list)


"""
    Example 5. Dictionary comprehension 1
"""
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(list(zip(names, heros)))

# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
my_dict = {name: hero for name, hero in zip(names, heros)}
print('Example 5: ', my_dict)


"""
    Example 6. Dictionary comprehension 2

    Filtering items with Dictionary comprehension
"""
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print('Example 6: ', my_dict)


"""
    Example 7. Set comprehension
"""
nums = [1, 1, 2, 1, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9, 10]
# my_set = set(nums)

# my_set = set()
# for num in nums:
#     my_set.add(num)
my_set = {num for num in nums}
print('Example 7: ', my_set)
