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
    #print("***Dataframe_1***:")
    #print(df1)
   
    ''' 1 - Read SPY data into temporary dataframe'''
    # 1.    Inform read_csv function that the date column
    #       should be used as index by using the index_col parameter
    # 2.    Convert data paremeter in datafra to DATETIME INDEX objects
    #       using parse_dates = True
   
    # First attempt
    # dfSPY = pd.read_csv('data/spy.csv')
   
    # Second attempt
    # dfSPY = pd.read_csv('data/spy.csv', index_col='Date', parse_dates = True)
    
    # Third version    
    dfSPY = pd.read_csv('data/spy.csv', index_col='Date', 
                        parse_dates = True, usecols = ['Date', 'Adj Close'],
                        na_values = ['nan'])
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})                        
                        
    # print("***Dataframe_2***:") 
    #print(dfSPY.head())   

    # Join the two dataframes using DataFrame.join()
    df1 = df1.join(dfSPY, how = 'inner')    
    # print("***Dataframe_2***:")
    
    ''' 2 - Read in more stocks'''
    symbols = ['GOOG', 'IBM', 'GLD']    
    for symbol in symbols:
        df_temp = pd.read_csv('data/{}.csv'.format(symbol), index_col = 'Date',
                              parse_dates = True, usecols = ['Date', 'Adj Close'],
                                na_values =['nan'])
        #rename to prevent crash
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        
        df1=df1.join(df_temp)
    
    # Drop NaN values - Method 1
    df1 = df1.dropna()
    print(df1)    
    
test_run_01_dfBuild()
