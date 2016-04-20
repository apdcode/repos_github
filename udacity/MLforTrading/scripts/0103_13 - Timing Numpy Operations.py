# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:53:16 2016
@author: apdcode
"""

'''0103    - The Power of NumPy'''

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import time

from time import time

os.chdir('C:/repos_github/udacity/MLforTrading/')
#os.chdir('C:/repos/research/data_misc')
os.listdir(os.getcwd())

'''0103_15 - Accessing array elements'''
def test_run():
    #t1 = time.time()
    #print("ML4T")
    #t2 = time.time()
    #print("Time", t2-t1, "seconds.")
    
    '''0103_14 - How fast is numpy?'''
def how_long(func, *args):    
    '''Execute function with given arguments, and measure execution time.'''    
    t0 = time()
    result = func(*args) # all arguments are passed in as-is
    t1 = time()
    return result, t1 - t0
    
def manual_mean(arr):
    """Compute mean (average) of all elemnts in the given 2d array."""
    sum = 0
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            sum = sum + arr[i,j]
    return sum / arr.size

'''0103_15 - Timing Numpy Operations'''



# Run it
if __name__ == "__main__":
    test_run()


