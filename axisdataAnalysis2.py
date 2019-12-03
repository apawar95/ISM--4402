#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


location = "desktop/datasets/axisdata.csv"
df = pd.read_csv(location)
df.head()


# In[2]:


df['Cars Sold'].mean()


# In[3]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[5]:


pd.pivot_table(df, values= ['Cars Sold'], index=['Gender'])


# In[6]:


df[df['Cars Sold'] >3]['Hours Worked'].mean()


# In[7]:


df['Years Experience'].mean()


# In[8]:


df[df['Cars Sold'] >3]['Years Experience'].mean()


# In[9]:


pd.pivot_table(df, values= ['Cars Sold'], index=['SalesTraining'])


# In[10]:


import matplotlib.pyplot as plt
import pandas as pd

names = ['Mary','Veronica','Tanya','india','Sam','Karen']
gender = ['Female','Male']
hoursworked = [43,34,28,36,30,48]
WorkList = zip(names,hoursworked)
df = pd.DataFrame(data = WorkList, columns=['Fnames', 'HoursWorked'])

get_ipython().magic(u'matplotlib inline')
df.plot(kind='bar')


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

names = ['Mary','Veronica','Tanya','india','Sam','Karen']
gender = ['Female','Male']
hoursworked = [43,34,28,36,30,48]

WorkList = zip(names,hoursworked)
columns=['Fnames', 'Hours Worked']
df = pd.DataFrame(data = WorkList, columns= columns)

df


# In[ ]:




