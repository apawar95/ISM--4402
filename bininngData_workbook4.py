#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[2]:


import pandas as pd

Location = "Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[3]:


import pandas as pd

Location = "Desktop/datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[5]:


bins = [0,80,100]
status_names ['Fail','Pass']
df ['status'] = pd.cut(df['grade'], bins, labels= status_names)
df


# In[6]:


bins = [0,80,100]
status_names = ['Fail','Pass']
df ['status'] = pd.cut(df['grade'], bins, labels= status_names)
df


# In[7]:


bins = [0,80,100]
status_names = ['Fail','Pass']
df ['status'] = pd.cut(df['grade'], bins, labels= status_names)
df


# In[8]:


pd.value_counts(df['status'])


# In[ ]:




