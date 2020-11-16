#!/usr/bin/env python3

import os
from datetime import datetime

# print(dir(os))

# Current Working Directory
print(os.getcwd())

# List files in Directory
print(os.listdir())

# Change Directory
os.chdir('/Users/Young/Desktop/')
print(os.getcwd())

# Make a Directory
os.mkdir('OS-Demo-2')
os.makedirs('OS-Demo-3/Sub-Dir-1')

# Remove a Directory
os.rmdir('OS-Demo-2')
os.removedirs('OS-Demo-3/Sub-Dir-1')

# Rename a File/Directory
# os.rename('test.rtf', 'test.txt')

# File status
# print(os.stat('test.txt'))

# mod_time = os.stat('test.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# Walk through directories
# path = '/Users/Young/Documents/Programming/ubuntu/practice'
# for dirpath, dirnames, filenames in os.walk(path):
#     print('Current Path: ', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()

# Get Environment Variables
# os.environ.get('HOME')

# A slash(/) is missing in the below file path
# file_path = os.environ.get('HOME') + 'test.txt'
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
