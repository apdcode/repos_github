# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import os
print (os.getcwd())

os.chdir('C:/repos_github/udacity/MLforTrading/data')

# Display first columns of df
def test_run():
    df = pd.read_csv('coint01.txt')
    print(df.head(2))    

# Display last columns of df
def test_run2():
    df = pd.read_csv('coint01.txt')
    print(df.tail(2)) 

# Select rows -> SLICING
def test_run3():
    df = pd.read_csv('coint01.txt')
    print(df[10:21]) 

# Compute max closing price

if __name__ == "__main__":
     test_run3()



