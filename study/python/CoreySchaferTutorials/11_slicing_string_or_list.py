#!/usr/bin/env python3


"""
    Example 1: Slicing a List
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Index    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# Neg    -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]
# end: non-inclusive
# step: default(1)

print('my_list[3:8]', my_list[3:8])
print('my_list[3:-2]', my_list[3:-2])
print('my_list[-7:-2]', my_list[-7:-2])

print('my_list[3:]', my_list[3:])
print('my_list[:-5]', my_list[:-3])
print('my_list[:]', my_list[:])

print('my_list[2:-1:2]', my_list[2:-1:2])
print('my_list[-3:2:-1]', my_list[-3:2:-1])
print('my_list[::-1]', my_list[::-1])


"""
    Example 2: Slicing a String
"""

sample_url = 'http://youngsappworkshop.com'
print('Sample url: ', sample_url)

# Reverse the url
print('Reverse the url: ', sample_url[::-1])

# Get the top level domain
print('Get the top level domain: ', sample_url[-4:])

# Print the url without the http://
print('Print the url without the http://: ', sample_url[7:])

# Print the url without the http:// nor the top level domain
print('Print the url without the http:// nor the top level domain: ', sample_url[7:-4])  # noqa
