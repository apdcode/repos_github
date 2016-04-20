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
# import time

# from time import time

os.chdir('C:/repos_github/udacity/MLforTrading/')
#os.chdir('C:/repos/research/data_misc')
os.listdir(os.getcwd())

'''0103_17 - Indexing an array with another array'''
def test_run():
    #a = np.random.rand(5)
    #print("Array:\n", a)
    # Accessing array using list of indices
    #indices = np.array([1,1,2,3])
    #print(a[indices])
       
    '''0103_17 - Indexing an array with another array'''
    a = np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,1,28,5,0)])
    #a = np.array([(20,25,), (1,2)])
    #print(a)
    
    # Calculating mean
    mean = a.mean()
    #print(mean)
    
    # masking
    print(a[a<mean])
    
    a[a<mean] = mean
    print(a)
    
# Run it
if __name__ == "__main__":
    test_run()


