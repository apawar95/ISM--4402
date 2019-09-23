#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
names = ['bob', 'jessica','mary', 'john','mel']
grades = [76, -2, 77, 78, 101]


# In[5]:


Gradelist = zip (names, grades)
df = pd.DataFrame(data = Gradelist,columns =['Names', 'Grade'])
df


# In[6]:


Gradelist = zip (names, grades)
df = pd.DataFrame(data = Gradelist,columns =['Names', 'Grade'])
df


# In[7]:


df.loc[(df['Grade'] >= 100, 'Grade')] = 100


# In[8]:


df.loc[(df['Grade'] >= 100, 'Grade')] = 100
df.loc [df['Grade'] <=0, ('Grade')] = 0
df


# In[ ]:




