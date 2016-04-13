# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:53:16 2016
@author: apdcode
"""

'''Build a datafram in pandas'''
import pandas as pd
import os

os.chdir('C:/repos_github/udacity/MLforTrading/')
#os.chdir('C:/repos/research/data_misc')
os.listdir(os.getcwd())


def test_run_01_dfBuild():
    # Define data range
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)
    # print(dates[0])
    
    # Create an empty dataframe
    df1 = pd.DataFrame(index=dates)
    print("***Dataframe_1***:")
    print(df1)
   
    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv('data/spy.csv')
    print("***Dataframe_2***:") 
    print(dfSPY.head())   

    # Join the two dataframes using DataFrame.join()
    df1 = df1.join(dfSPY)    
    print("***Dataframe_2***:")
    print(df1)
    
test_run_01_dfBuild()
