#!/usr/bin/env python3

"""
    Example. Basic Syntax Working with files
        - Not Recommended
"""
# f = open('LICENSE', 'r')
# print(f.mode)
# f.close()


"""
    Example. Working with files using Context Manager
        - Automatically closes the files
        - Closes files on Exceptions
        - Recommended
"""
# Reading a File
with open('LICENSE', 'r') as f:
    """
        Reading file contents
    """
    # Read the entire contents of a file
    # f_contents = f.read()

    # Read 100 characters and return a String
    # f_contents = f.read(100)

    # print(type(f_contents))
    # Read all lines of a file and return a List
    # f_contents = f.readlines()

    # Read a line of a file and return a String
    # f_contents = f.readline()

    """
        Iterate through the file
    """
    # Iterate through all lines of a file
    # for line in f:
    #     print(line, end='')

    # Iterate through while loop
    # size_to_read = 100
    # f_contents = f.read(size_to_read)
    # while len(f_contents) > 0:
    #     print(f_contents, end='')
    #     f_contents = f.read(size_to_read)

    """
        Getting/Setting Position
    """
    # Getting current position
    # print(f.tell())
    # size_to_read = 100
    # f_contents = f.read(size_to_read)
    # print(f.tell())

    # Setting position
    # f.seek(50)
    # print(f.tell())
    # f_contents = f.read(size_to_read)
    # print(f_contents)
    pass

# Writing a File
# with open('test.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')


"""
    Example. Read and Write Files
"""
# Copying a Text file
# with open('LICENSE', 'r') as rf:
#     with open('test.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# Open Files in Binary mode
with open('rabbit.jpg', 'rb') as rf:
    with open('rabbit_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
