#!/usr/bin/env python3


# There is NO switch-case statements in Python


# Comparisons:
#   Equal:            ==
#   Not Equal:        !=
#   Greater Than:     >
#   Less Than:        <
#   Greater or Equal: >=
#   Less or Equal:    <=
#   Object Identity:  is


# False Values:
#   False
#   None
#   Zero of any numeric type
#   Any empty sequence. For example, '', (), [].
#   Any empty mapping. For example, {}.


language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')


# and   or   not
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')


if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


# Object Identity:  is
a = [1, 2, 3]
# b = [1, 2, 3]
b = a

print(a == b)
print(id(a))
print(id(b))
print(a is b)


# False Values:
#   False
#   None
#   Zero(0) of any numeric type
#   Any empty sequence. For example, '', (), [].
#   Any empty mapping. For example, {}.

condition = {}

if condition:
    print('Evaluated to True: ', condition)
else:
    print('Evaluated to False: ', condition)
