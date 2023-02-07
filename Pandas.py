#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install plotly')


# In[7]:


import pandas as pd


# In[81]:


df = pd.read_csv(r"C:\Users\user\Desktop\data\survey_results_public.csv")
schema_df = pd.read_csv(r"C:\Users\user\Desktop\data\survey_results_schema.csv")


# In[38]:


df


# In[14]:


df.shape


# In[15]:


df.info()


# In[16]:


df.head()


# In[17]:


df.tail()


# In[41]:


schema_df


# In[40]:


pd.set_option('display.max_columns', 79)
pd.set_option('display.max_rows', 79)


# In[82]:


df.columns


# Getting one row

# In[84]:


df.iloc[1]


# Getting two (2) rows

# In[103]:


df.iloc[[0, 1, 2]]


# In[106]:


df.iloc[[1, 2], 5]


# In[107]:


df["EdLevel"].value_counts()


# In[108]:


df["EdLevel"]


# In[109]:


df.loc[2]


# In[110]:


df["Country"].value_counts()


# In[114]:


df.loc[0: 30, "CodingActivities"]


# In[116]:


df.loc[0: 10, "MainBranch": "LearnCode"]


# In[115]:


df["CodingActivities"].value_counts()


# In[88]:


df[["ResponseId", "MainBranch", "Employment"]]


# In[ ]:




