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
    a = np.random.rand(5,4)
    print("Array:\n", a)

    # assigning a value to a particular location
    #a[0,0] = 1
    #a[1,0] = 2
    #a[1,1] = 3
    #a[1,2] = 4
    #print("\nModified one elment:\n",a)

    #0 - Assigning values to rows and columns

    #1 - whole matrix    
    a[:] = 1
    print("\nModified a lot of elements:\n",a)    
    
    #2 - first row
    #a[:,0] = 5
    #print("\nModified a lot of elements:\n",a)    
    
    #3 - second column
    #a[:,1] = 5
    #print("\nModified a lot of elements:\n",a)        
    
    #4 - third column
    #[:,2] = 5
    #print("\nModified a lot of elements:\n",a)            
    
    #5 - second and third column
    #a[:,1:2] = 5
    #print("\nModified a lot of elements:\n",a)                
    
    #6 - From second to the last column
    #a[:,1:] = 5
    #print("\nModified a lot of elements:\n",a)                    
    
    #7 - From second to the third row
    #a[1:3,] = 5
    #print("\nModified a lot of elements:\n",a)        
    
    #8 - From the second to the third row in the second to the thir column
    #a[1:3,1:3] = 5
    #print("\nModified a lot of elements:\n",a)        
    
    #9 - Assign list of values to column
    a[:,3] = [1,2,3,4,5]
    print("\nModified a lot of elements:\n",a)            
    
        
    
# Run it
if __name__ == "__main__":
    test_run()


