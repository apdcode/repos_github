# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:53:16 2016
@author: apdcode
"""

'''0103    - The Power of NumPy'''
# %reset

"""SETTINGS"""
import pandas as pd
import os
import matplotlib.pyplot as plt

"""CONFIGS"""
os.chdir('C:/repos_github/udacity/MLforTrading/')
#os.chdir('C:/repos/research/data_misc')
os.listdir(os.getcwd())
start_date = '2010-01-01'
end_date = '2010-12-31'
dates = pd.date_range(start_date, end_date)
symbols = ['SPY', 'XOM', 'GOOG', 'GLD']

"""FUNCTIONS"""
def symbol_to_path(symbol, base_dir='data'):
    """Return CSV file path given ticker symbol"""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))
   
def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols for CSV files."""
    df = pd.DataFrame(index = dates)
    if 'SPY' not in symbols:    # add SPY for reference if absent
        symbols.insert(0, 'SPY') 
        
    for symbol in symbols:
        #print(symbol)
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
    plt.show()

def normalize_data(df):
    """Normalize stock prices using the first row of the data frame."""
    return df/df.ix[0,:]

"""0104_04"""
"""Global statistcs"""
#df1 = normalize_data(get_data(symbols, dates))
#plot_data(df1)
#print(df1.mean(), '\n', '\n', df1.median(), '\n', '\n',df1.std())

"""0104_05"""
"""Rolling statistics"""

"""0104_06"""
"""Which statistics ot use?"""

"""0104_07"""
"""Bollinger Bands"""

"""0104_08"""
"""Computing rolling statistics"""
def test_run_0104_08():
    # Read Data
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    
    # Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title = 'SPY rolling mean', label = 'SPY')
    
    # Compute rolling mean using a 20-day window
    rm_SPY1 = pd.rolling_mean(df['SPY'], window = 20)
    rm_SPY2 = pd.rolling_mean(df['SPY'], window = 40)
    rm_SPY3 = pd.rolling_mean(df['SPY'], window = 60)
    #rm_SPY = pd.rolling_mean(df['SPY'], window = 40)
    #rm_SPY = pd.rolling_mean(df['SPY'], window = 60)
    
    # Add rolling mean to same plot
    rm_SPY1.plot(label='Rolling Mean', ax = ax)
    rm_SPY2.plot(label='Rolling Mean', ax = ax)
    rm_SPY3.plot(label='Rolling Mean', ax = ax)
    
    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc = 'upper left')
    plt.show
    
"""0104_09"""
"""Quiz - Calculate Bollinger Bands"""    

def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""    
    
    return pd.rolling_mean(values, window)    
    
def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    
    return pd.rolling_std(values, window)

def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands"""
    
    upper_band = rm + rstd*4    
    lower_band = rm - rstd*4    
    
    return upper_band, lower_band

def test_run_get_bollinger_bands():
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)

    # Compute bollinger bands
    # 1. Compute rolling mean
    rm_SPY = get_rolling_mean(df['SPY'], window = 20)

    # 2. Compute  rolling standard deviation
    rstd_SPY = get_rolling_std(df['SPY'], window = 20)   
    
    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)
    
    # Plot raw SPY values, rolling mean and bollinger bands
    ax = df['SPY'].plot(title="Bollinger Bands", label = 'SPY')
    rm_SPY.plot(label='Rolling Mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)
    
    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show
      
    
"""ACTIONS"""
test_run_0104_08()
# test_run_get_bollinger_bands()

  
    

    
