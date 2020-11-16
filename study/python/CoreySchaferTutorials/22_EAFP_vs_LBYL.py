#!/usr/bin/env python3

"""
    Duck Typing
        - Assume an object is a duck if it walks like a duck
        and quacks like a duck
        - It doesn't matter what type of object it is, it matters
        what the object can do what it is asked to do
"""

"""
    EAFP versus LBYL
    https://blogs.msdn.microsoft.com/pythonengineering/2016/06/29/idiomatic-python-eafp-versus-lbyl/
"""


class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    """ Example 1: Pythonic
            - Easier to Ask Forgiveness than Permission (EAFP)
    """
    try:
        thing.quack()
        thing.fly()
        # thing.bark()
    except AttributeError as e:
        print(e)


# def quack_and_fly(thing):
#     """ Example 2: Non-Pythonic
#             - Not Duck-Typed
#     """
#     if isinstance(thing, Duck):
#         thing.quack()
#         thing.fly()
#         print()
#     else:
#         print('This has to be a Duck!')


# def quack_and_fly(thing):
#     """ Example 3: Non-Pythonic
#             - Look Before You Leap (LBYL)
#     """
#
#     if hasattr(thing, 'quack'):
#         if callable(thing.quack):
#             thing.quack()
#
#     if hasattr(thing, 'fly'):
#         if callable(thing.fly):
#             thing.fly()
#     print()


duck = Duck()
quack_and_fly(duck)

person = Person()
quack_and_fly(person)


"""
    More Example
"""
# person = {'name': 'Jessy', 'age': 24, 'job': 'Developer'}
person = {'name': 'Jessy', 'age': 24}

# EAFP (Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print("Missing {} key".format(e))

# LBYL (Non-Pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
else:
    print('Missing some keys.')
