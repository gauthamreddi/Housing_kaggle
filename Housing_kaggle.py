#!/usr/bin/env python
# coding: utf-8

# In[12]:


# import libraries
import os
import pandas as pd
import numpy as np
import seaborn as sns # for visualization
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy.stats import norm 
from scipy import stats # for statistics
from sklearn.preprocessing import StandardScaler


# In[8]:


os.chdir("E:Housing_project")


# In[9]:


Housing_prices=pd.read_csv("./train.csv")


# In[10]:


Housing_prices.shape


# In[14]:


Housing_prices.head()


# In[15]:


Housing_prices.describe()


# In[16]:


Housing_prices.info()


# In[17]:


Housing_prices.isna().sum()


# In[20]:


totalcells=np.product(Housing_prices.shape)
# Count number of missing values per column
missingcount=Housing_prices.isnull().sum()
# Calculate total number of missing values
totalMissing=missingcount.sum()
# Calculate percentage of missing values
print("This Data contains", round(((totalMissing/totalcells)*100),2),"%"," of missing values.")


# In[22]:


# Percentage of missing values in each column
(Housing_prices.isnull().sum() / len(Housing_prices))*100


# In[21]:


# Identify the columns which have null values
sns.heatmap(Housing_prices.notnull(),yticklabels=False,cbar=False, cmap='viridis')


# In[ ]:




