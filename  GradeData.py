#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
location = "datasets/gradedata.xlsx"
df = pd.read_excel(location)


# In[2]:


df.columns = ['first', 'last', 'sex', 'age', 'excer', 'hrs', 'grd', 'addr']
df.head()


# In[ ]:




