# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import os
print (os.getcwd())

os.chdir('C:/repos_github/udacity/MLforTrading/data')
os.chdir('C:/repos/research/data_misc')
os.listdir(os.getcwd())

# Display first columns of df
def get_max_close(symbol):
    """Return the maximum closing value for stock indicated by symbol
    
        Note: Data is stored in file Coint01.txt
    """
    
    df = pd.read_csv('{}.txt'.format(symbol))
    return df['Close'].max()


def test_run():
    for symbol in ['ENOYZ7', 'F1BYF7']:
        print ('Max close')
        print (symbol, get_max_close(symbol))
        #print (symbol)

test_run()