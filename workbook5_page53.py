#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 

location = "Desktop/datasets/gradedata.csv"
df = pd.read_csv (location)
df.tail()


# In[2]:


import pandas as pd 
import numpy as np 

location = "gradedata.csv"
df = pd.read_csv (location)
df.tail()


# In[3]:


df.take(np.random.permutation(len(df))[:500]) 


# In[ ]:




