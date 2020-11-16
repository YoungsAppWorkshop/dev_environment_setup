#!/usr/bin/env python3
import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


x = pd.read_csv(BASE_DIR + '/data/IBM.csv')
print(x[1:3])
