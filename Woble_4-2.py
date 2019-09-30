#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "Datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


import numpy as np
df['isBusy'] = np.where((df['exercise']>3) 
                     &  (df['hours']>17),'yes', 'no')
df.tail(10)


# In[ ]:




