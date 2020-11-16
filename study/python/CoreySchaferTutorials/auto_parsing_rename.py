#!/usr/bin/env python3

import os

os.chdir('/Users/Young/Desktop/Ani')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    if file_name[0] != '.':
        f_title, f_course, f_num = file_name.split('_')
        new_name = '{}_{}_{}{}'.format(f_num, f_title, f_course, file_ext)
        os.rename(f, new_name)
