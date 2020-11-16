#!/usr/bin/env python3

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# Raw String i.e. r'string'
# Python doesn't handle special characters in a Raw String
# print('\tTab') vs print(r'\tTab')


"""
    Example 1. Literal Search
"""
# pattern = re.compile(r'abc')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)


"""
    Example 2. Pattern Search
"""
# Character Sets: []
# [a-z]: a character from a to z
# [^a-z]: a character except a to z
# [-.*]: - or . or *

# pattern = re.compile(r'\d{3}[-.*]\d{3}[-.*]\d{4}')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# Phone Number Example
# with open('Regex/data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     pattern = re.compile(r'\d{3}[-.*]\d{3}[-.*]\d{4}')
#     matches = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)

# Email example
# with open('Regex/emails.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
#     matches = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)

# Ignore Case
# pattern = re.compile(r'start', re.IGNORECASE)
# pattern = re.compile(r'start', re.I)

# URLs example
with open('Regex/urls.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
    matches = pattern.finditer(contents)

    # pattern.sub() method
    # subbed_url = pattern.sub(r'\2\3', contents)
    # print(subbed_url)

    for match in matches:
        # match.group() method:
        # group: 0 entire match
        # group: 1 ~ 3 each group in the match
        print(match.group(3))
