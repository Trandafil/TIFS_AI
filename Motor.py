#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("measures_v2.csv")
df


# In[3]:


X = df.drop(['pm'], axis=1).values
y=df['pm'].values


# In[4]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression


# In[5]:


X_train, X_test, y_train, y_test=train_test_split(X, y)


# In[6]:


linear = LinearRegression()
linear.fit(X_train, y_train)
y_pred=linear.predict(X_test)


# In[7]:


mean_squared_error(y_pred, y_test)


# In[8]:


plt.scatter(y_pred, y_test)


# In[9]:


from sklearn.preprocessing import StandardScaler


# In[10]:


scaler=StandardScaler()
X_train_tr=scaler.fit_transform(X_train)
X_test_tr=scaler.transform(X_test)


# In[11]:


linear = LinearRegression()
linear.fit(X_train_tr, y_train)
y_pred_tr=linear.predict(X_test_tr)


# In[12]:


mean_squared_error(y_pred_tr, y_test)


# In[ ]:




