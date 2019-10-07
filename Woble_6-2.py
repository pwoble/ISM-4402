#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "Datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


def score_to_numeric(x):
    if x=='female':
        return 1
    if x=='male':
        return 0


# In[3]:


df['gender_val'] = df['gender'].apply(score_to_numeric)
df.tail()


# In[5]:


df_gender = pd.get_dummies(df['gender'])
df_gender.tail()


# In[6]:


df_new = pd.concat([df, df_gender], axis=1)
df_new.tail()
df_new = df.join(df_gender)
df_new.tail()


# In[8]:


import statsmodels.formula.api as sm
result = sm.ols(
        formula='grade ~ age + exercise + hours',
        data=df).fit()
result.summary()


# In[9]:


import statsmodels.formula.api as sm
result = sm.ols(
        formula='grade ~ exercise + hours',
        data=df).fit()
result.summary()


# In[10]:


import statsmodels.formula.api as sm
result = sm.ols(
        formula='grade ~ gender_val + exercise + hours',
        data=df).fit()
result.summary()


# In[ ]:




