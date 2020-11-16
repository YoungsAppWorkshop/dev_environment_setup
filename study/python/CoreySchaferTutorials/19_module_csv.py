#!/usr/bin/env python3

import csv


"""
    Example 1: Using CSV Reader/Writer
"""
# with open('names.csv', 'r') as csv_file:
#     # Read the csv_file
#     csv_reader = csv.reader(csv_file)
#
#     # Jump to the second line of the csv_file
#     # next(csv_reader)
#
#     with open('new_names.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#
#         for line in csv_reader:
#             csv_writer.writerow(line)


"""
    Example 2: Using DictReader/DictWriter
"""
with open('names.csv', 'r') as csv_file:
    # Read the csv_file using DictReader
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line['email'])

    with open('new_names.csv', 'w') as new_file:
        # To remove email field,
        # fieldnames = ['first_name', 'last_name']
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file,
                                    fieldnames=fieldnames,
                                    delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            # To remove email field,
            # del line['email']
            csv_writer.writerow(line)
