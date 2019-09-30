#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
Location = "Datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[4]:


#create the bin divider
bins = [0,80,100]
#create names for the groups
group_names = ['Fail','Pass']


# In[5]:


df['passorfail'] = pd.cut(df['grade'], bins, labels = group_names)
df


# In[6]:


pd.value_counts(df['passorfail'])


# In[ ]:




