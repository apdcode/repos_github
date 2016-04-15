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

os.chdir('C:/repos_github/udacity/MLforTrading/')
#os.chdir('C:/repos/research/data_misc')
os.listdir(os.getcwd())

'''Lect_0103_06 - Creating NumPy arrays'''
def test_run():
    '''List to 1D array'''
    # print(np.array([2,3,4]))

    '''2D array'''
    # print(np.array([(2,3,4), (5,6,7)]))

    '''Empty array, nope -> array with slots filled with memory address'''
    # print ('empty? ',np.empty(1))
    # print (np.empty((5,4)))

    '''Lect_0103_07 - Arrays with initial values'''
#   Array of 1s
    # print(np.ones((5,4), dtype=np.int_))

    '''Lect_0103_07 - Generating random numbers'''
#   Generate an array of randoms, uniformly sampled from [0.0, 1.0)
    # print(np.random.random((8,4)))                                            # this is a tuple
    # print(np.random.rand(8,4))                                                # this is not a tuple

#   Sample numbers from a Gaussian (normal) distribution
    print(np.random.normal(size = (2,3))                                        # standard normal with mean = 0, sd = 1
    

# Run it
if __name__ == "__main__":
    test_run()


