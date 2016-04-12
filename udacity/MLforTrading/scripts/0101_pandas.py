# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import os
print (os.getcwd())

path_scripts = 'C:\repos_github\udacity\MLforTrading\data'

os.chdir('C:/repos_github/udacity/MLforTrading/data')


def test_run():
    df = pd.read_csv