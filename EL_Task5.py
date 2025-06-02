#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv('../DataSets/SHOES.csv')
df


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df.Sales=df.Sales.replace("[$,]","",regex=True).astype('int64')
df.Inventory=df.Inventory.replace("[$,]","",regex=True).astype('int64')
df.Returns=df.Returns.replace("[$,]","",regex=True).astype('int64')


# In[6]:


df


# In[7]:


df.describe()


# In[8]:


df.Region.value_counts()


# In[9]:


df.Product.value_counts()


# In[10]:


df.Subsidiary.value_counts()


# In[11]:


sns.heatmap(df[['Stores','Sales','Inventory','Returns']].corr(),annot=True, cmap='coolwarm')
plt.show()


# In[12]:


sns.pairplot(df[['Stores','Sales','Inventory','Returns']])
plt.show()


# In[17]:


sns.histplot(df.Region)
plt.xticks(rotation=90)
plt.show()


# In[18]:


sns.scatterplot(x=df.Inventory,y=df.Sales)
plt.show()


# In[19]:


sns.scatterplot(x=df.Returns,y=df.Sales)
plt.show()


# In[20]:


sns.boxplot(df)


# In[21]:


i='Inventory'
q3=np.percentile(df[i],75)
q1=np.percentile(df[i],25)
iqr=q3-q1
c1=q1-1.5*(iqr)
c2=q3+1.5*(iqr)


# In[22]:


o=df[(df[i]>c2)|(df[i]<c1)]
o


# In[23]:


o = o.index


# In[24]:


o


# In[25]:


df = df.drop(labels=o)
df

