# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:53:16 2016
@author: apdcode
"""

'''0103    - The Power of NumPy'''
# %reset

import pandas as pd
import os
import matplotlib.pyplot as plt

os.chdir('C:/repos_github/udacity/MLforTrading/')
#os.chdir('C:/repos/research/data_misc')
os.listdir(os.getcwd())
start_date = '2010-01-01'
end_date = '2010-12-31'
dates = pd.date_range(start_date, end_date)


def symbol_to_path(symbol, base_dir='data'):
    """Return CSV file path given ticker symbol"""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))
   
def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols for CSV files."""
    df = pd.DataFrame(index = dates)
    if 'SPY' not in symbols:    # add SPY for reference if absent
        symbols.insert(0, 'SPY') 
        
    for symbol in symbols:
        print(symbol)
        # Read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col ='Date',
                              parse_dates = True,
                              usecols = ['Date', 'Adj Close'], na_values = ['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})  
            
        df = df.join(df_temp)
        if symbol == 'SPY': # drop dates where SPY did not trade
           df = df.dropna(subset = ["SPY"])
           
    return df
    
    
def plot_data(df, title ="Stock Prices"):
    '''Plot stock price'''
    ax = df.plot(title = title, fontsize = 10)
    ax.set_xlabel("Date")    
    ax.set_ylabel("Price")
    #plt.show()

#def plot_selected(df, columns, start_index, end_index):
#    """Plot the desired columns over index values given in the range."""
#    plot_data(df.ix[start_index:end_index, columns], title ="Selected data")
#
#plot_selected()

plot_data(df1)    
    
def normalize_data(df):
    """Normalize stock prices using the first row of the data frame."""
    
    return df/df.ix[0,:]
    
def test_run():
    # Define a date range
    dates = pd.date_range(start_date, end_date)

    # Choose stock symbols
    symbols = ['SPY', 'XOM', 'GOOG', 'GLD']
    
    # Get stock data    
    # slice by row range (dates) using DataFrame.ix[] selector
    df = get_data(symbols,  dates)
    plot_data(df)
    return df
    
df1 = test_run()