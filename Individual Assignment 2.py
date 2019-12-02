#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[4]:


df['Cars Sold'].mean()


# In[6]:


df['Cars Sold'].max()


# In[7]:


df['Cars Sold'].min()


# In[8]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[9]:


df[df['Cars Sold'] > 3] ['Hours Worked'].mean()


# In[10]:


df['Years Experience'].mean()


# In[11]:


df[df['Cars Sold'] > 3] ['Years Experience'].mean()


# In[12]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[18]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
plt.scatter(df['Hours Worked'], df['Cars Sold'])


# In[48]:


df = pd.read_csv(Location)


# In[47]:





# In[51]:


df.hist(column="Cars Sold", by="SalesTraining")


# In[ ]:





# In[ ]:




