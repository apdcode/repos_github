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

'''0103_19 - Arithmetic Operations'''
def test_run():
   
    a = np.array([(1,2,3,4,5),(10,20,30,40,50)])
    #print("Original array a:\n",a)
    
    # Multiply a by 2
    #print("Multiply a by 2:\n",a*2)

    # Division by 2
    print("Division by 2:\n",a/2)
    
    # Integer Division by 2
    print("Integer division by 2:\n",a//2)
    
    # How about mathemtic operations using two arrays
    b = np.array([(100,200,300,400,500), (1,2,3,4,5)])
    
    # Add arrays a and b
    print(a+b)    
    
    
    
    
# Run it
if __name__ == "__main__":
    test_run()


