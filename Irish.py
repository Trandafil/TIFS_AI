#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('Iris.csv')
df


# In[3]:


X = df.drop(['Species', 'Id'], axis=1).values
y = df['Species'].values


# In[4]:


from sklearn.model_selection import train_test_split


# In[5]:


X_train, X_test, y_train, y_test=train_test_split(X, y)


# In[6]:


from sklearn.linear_model import LogisticRegression


# In[7]:


logit = LogisticRegression(max_iter=1000)
logit.fit(X_train, y_train)


# In[8]:


y_pred = logit.predict(X_test)


# In[9]:


y_pred


# In[10]:


from sklearn.metrics  import  accuracy_score


# In[11]:


accuracy_score(y_test, y_pred)


# In[ ]:




