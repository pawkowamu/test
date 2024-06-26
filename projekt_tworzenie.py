#!/usr/bin/env python
# coding: utf-8

# In[1]:


# System wspomagania decyzji inwestorskich
# Paweł Kowalski


# In[2]:

# sprawdzenieczasu działania programu
import time as tm
start_time = tm.time()


# In[3]:


# import bibliotek
import yfinance as yf
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib 
import sklearn  
import statsmodels 
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression
from plik_tickers import tickers 


# In[4]:


# Sprawdzanie wersji Phytona
import sys 
print(f"Python: {sys.version}")


# In[5]:


# Sprawdzanie wersji bibliotek
print(f"yfinance: {yf.__version__}")
print(f"numpy: {np.__version__}")
print(f"matplotlib: {matplotlib.__version__}")
print(f"tensorflow: {tf.__version__}")
print(f"scikit-learn: {sklearn.__version__}")
print(f"seaborn: {sns.__version__}")
print(f"statsmodels: {statsmodels.__version__}")

