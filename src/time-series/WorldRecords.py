#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Import the necessary files
import pandas as pd


# In[4]:


# Read the tables
tables = pd.read_html("https://en.wikipedia.org/wiki/1500_metres_world_record_progression")
table = tables[1]


# In[5]:


# Demonstrate how tables look like with indices etc


# In[6]:


# Read times and dates from one table only
# Pre-coded example
times=table['Time']
dates=table['Date']
dates = pd.to_datetime(dates)
dates.max()-dates.min()


# In[7]:


# Pick one record set
import numpy as np
#import datetime
n_records = len(times)
years = np.zeros(n_records) # create zero years
seconds = np.zeros(n_records) # create zero years
for i in range(n_records):   
    years[i] = dates[i].date().year
    tmp = times[i].replace("+","0").split(':')
    seconds[i] = float(tmp[0])*60+float(tmp[1])


# In[8]:


import matplotlib.pyplot as plt
plt.plot(years[0:15], seconds[0:15])
plt.plot(years, seconds)
plt.axis([1910, 2022, 200, 240])
plt.xlabel("year")
plt.ylabel("time (s)")
plt.show()





