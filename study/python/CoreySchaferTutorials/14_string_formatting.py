#!/usr/bin/env python3

import datetime

person = {'name': 'Jenn', 'age': 23}
my_list = ['Jenn', 23]

"""
    Example 1.
        - Various ways of Formatting a String
"""
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'  # noqa
sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])  # noqa
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])  # noqa
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(my_list)
print(sentence)


"""
    Example 2.
"""
tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)


"""
    Example 3.
        - Formatting with keys
"""
sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')  # noqa
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)


"""
    Example 4.
        - Formatting with attributes
"""


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)


"""
    Example 5.
        - Formatting Numbers
"""
for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)


pi = 3.14159265

sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)


sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)


"""
    Example 6.
        - Formatting Date/Time
"""

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

# March 01, 2016

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)  # noqa
print(sentence)
