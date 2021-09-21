# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:39:43 2021

@author: lzt68
"""

#%% read the data
import pandas as pd
import numpy as np
data=pd.read_csv("bank-full.csv",sep=';',engine="python")

#%% add year
data['year'] = np.zeros(data.shape[0])
year_counter = 2008
ii = 0
while ii <= data.shape[0] - 1:
    if data['month'].iloc[ii] != 'jan':
        data['year'].iloc[ii] = year_counter
        ii = ii + 1 
    else:
        year_counter = year_counter + 1
        for jj in range(ii, data.shape[0]):
            if data['month'].iloc[jj] == 'jan':
                data['year'].iloc[jj] = year_counter
            else:
                ii = jj
                break
    
#%% add timestamp
data['month'].replace({"jan": "01", "feb": "02", "mar": "03",
                       "apr": "04", "may": "05", "jun": "06",
                       "jul": "07", "aug": "08", "sep": "09",
                       "oct": "10", "nov": "11", "dec": "12"},
                     inplace = True)

data['year'] = data['year'].astype(int).astype(str)
data['day'] = data['day'].astype(str)

data['timestamp'] = data.apply(lambda x: x['day'] + "-" + x['month'] + "-" + x['year'], axis=1)
data['timestamp'] = pd.to_datetime(data['timestamp'], format="%d-%m-%Y")

#%% match timestamp to weekday
data['weekday'] = data['timestamp'].dt.dayofweek
data.head()

#%% export the data
data.to_csv("bank-full-add_timestamp.csv", index = False)