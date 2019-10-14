#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 

location =  "gradedata.csv"

df = pd.read_csv (location)
df.head()


# In[2]:


df = df.sort_values(by= ['lname','age', 'grade'] ,ascending= [True, True, False])
df.head()


# In[3]:


df = df.sort_values(by= ['lname','age', 'grade'] ,ascending= [True, True, True])
df.head()


# In[ ]:




