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

    '''Lect_0103_09 - Generating random numbers'''
#   Generate an array of randoms, uniformly sampled from [0.0, 1.0)
    # print(np.random.random((8,4))) # this is a tuple
    # print(np.random.rand(8,4))# this is not a tuple

#   Sample numbers from a Gaussian (normal) distribution
    # print(np.random.normal(size = (10,10))) # standard normal with mean = 0, sd = 1
    
#   Now, change the mean and standard deviation
    # print(np.random.normal(50,10, size = (10,10)))

    '''Lect_0103_10 - Array Attributes'''
    a = np.random.random((5,4)) # 5x4 array of random numbers
    # print(a)
    #print(a.shape)
    #print(a.shape[0])
    #print(a.shape[1])
    #print(len(a.shape))
    #print(a.size)
    print(a.dtype)
    
    '''Lect_0103_11 - Operations on ndarrays'''
#   Random seed
    np.random.seed()
    a = np.random.randint(0,10,size=(5,4))
    #print("Array:\n\n\n ",a)

#   Sum of all elements
    #print("Sum of all elements:", a.sum())

#   Iterate over rows, to compute sum of each column
    #print("Sum of each column: ",a.sum(axis=0))

#   Iterate over columns to compute sum of each row
    #print("Sum of row: ", a.sum(axis=1))
    
#   Statistics: min, max, mean
    #print("Minimum of each column:\n", a.min(axis=0))
    #print("Maximum of each row:\n", a.max(axis=1))
    #print("Mean of all elements:\n", a.mean())

    '''Lect_0103_12 - QUIZ - Locate maximum value'''
def get_max_index(a):
        """Return the index of the maximum value in  given 1D array"""
        # a = np.array([9,6,200,3,14,7,19], dtype =np.int32)        
        return a.argmax()
        

def test_run_get_max_index():
        a = np.array([9,600,2,3,14000,7,19], dtype =np.int32)
        #print("it runs")        
        #print(get_max_index(a))
# test_run_get_max_index()    
        
        '''Lect_0103_13 - Timing python operations'''       
    
    
# Run it
if __name__ == "__main__":
    test_run()


