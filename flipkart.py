#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


flip_data=pd.read_csv('flipkart_com-ecommerce_sample.csv')


# In[3]:


print(flip_data)


# In[4]:


print(flip_data.head())


# In[5]:


print(flip_data.tail())


# In[6]:


print(flip_data.shape)


# In[7]:


print(flip_data.columns)


# In[8]:


print(flip_data.describe())


# In[9]:


print(flip_data.isnull())


# In[10]:


print(flip_data.columns)


# In[11]:


print(flip_data.info())


# In[12]:


print(flip_data.corr())


# In[13]:


prepared_data=flip_data


# In[14]:


print(prepared_data.head)


# In[15]:


print(prepared_data.columns)


# In[16]:


predict_variable=prepared_data['product_name']


# In[17]:


print(predict_variable)


# In[18]:


predict_variable=prepared_data['pid']


# In[19]:


print(predict_variable)


# In[20]:


predict_variable=prepared_data['image']
print(predict_variable)


# In[21]:


print(prepared_data.columns)


# In[22]:


print(prepared_data.plot(kind='line',x='product_name',y='retail_price',title='product_name vs retail_price'))


# In[23]:


print(prepared_data.plot(kind='scatter',x='product_name',y='retail_price',title='product_name vs retail_price'))


# In[24]:


print(prepared_data.plot(kind='bar',x='product_name',y='retail_price',title='product_name vs retail_price'))


# In[25]:


print(prepared_data.plot(kind='area',x='product_name',y='retail_price',title='product_name vs retail_price'))


# In[26]:


print(prepared_data.plot(kind='box',x='product_name',y='retail_price',title='product_name vs retail_price'))


# In[27]:


print(prepared_data.plot(kind='hist'))


# In[28]:


print(prepared_data.columns)


# In[29]:


predict_data=prepared_data['product_category_tree']
print(predict_data)


# In[30]:


predict_data=prepared_data['discounted_price']
print(predict_data)


# In[31]:


print(prepared_data.plot(kind='line',x='product_name',y='discounted_price',title='product_price vs discounted_price'))


# In[32]:


print(prepared_data.plot(kind='scatter',x='product_name',y='discounted_price',title='product_name vs discounted_price'))


# In[33]:


print(prepared_data.plot(kind='bar',x='product_name',y='discounted_price',title='product_name vs discounted_price'))


# In[34]:


print(prepared_data.plot(kind='area',x='product_name',y='discounted_price',title='product_name vs discounted_price'))


# In[35]:


print(prepared_data.plot(kind='box',x='product_name',y='discounted_price',title='product_name vs discounted_price'))


# In[36]:


print(prepared_data.plot(kind='hist'))


# In[38]:


print(prepared_data.columns)


# In[ ]:




