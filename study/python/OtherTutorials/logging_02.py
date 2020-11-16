#!/usr/bin/env python3
# Python Programming - logging

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:
    """ A Sample Employee Class """

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname,
                                                       self.email))

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer')
emp_2 = Employee('Young', 'Jung')
emp_3 = Employee('Jane', 'Dow')
