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

'''0103_15 - Accessing array elements'''
def test_run():
    a = np.random.rand(5,4)
    # print("Array:\n", a)

    # Accessing element at position (3,2)
    # element=a[3,2]
    # print(element)

    # Elements in defined range -> SLICING
    # print(a[0,1:3])

    # Subset of array
    # Sline n:m:t specifies a range that starts at n
    # and stops before m, in t steps
    print(a[:,0:3:2]) # will select columns 0,2 for every row

# Run it
if __name__ == "__main__":
    test_run()


