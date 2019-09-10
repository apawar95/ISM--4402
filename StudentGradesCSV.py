#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/smallgradesh.csv"
df = pd.read_csv(Location, header=None)


# In[8]:


import pandas as pd
Location = "datasets/smallgradesh.csv"
df = pd.read_csv(Location, header=None)
df.head()


# In[9]:


df.columns = ['Names','Grades']
df.head()


# In[4]:


import pandas as pd
names= ['bob', 'jessica', 'mary','john', 'mel']
grades = [76, 95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns= ['Name, Games'])
df.head() 


# In[5]:


import pandas as pd
names = ['bob', 'jessica', 'mary','john', 'mel']
grades = [76, 95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns= ['Name', 'Games'])
df.head() 


# In[6]:


df.to_csv('studentgrades.csv',index=Flase,header=true)


# In[7]:


df.to_csv('studentgrades.csv',index=False, header= True) 


# In[ ]:




