#!/usr/bin/env python
# coding: utf-8

# In[32]:


# import the pandas library.
import pandas as pd


# In[33]:


# load the CSV file using the read_csv() function.
data = pd.read_csv('E:\\Main Flow Services and Technologies\\TASKS\\DATA_ANALYSIS_WITH_PYTHON-ID-11896\\TASK 2\\01.Data Cleaning and Preprocessing.csv')


# In[34]:


# type function to see the type of our data.
type(data)


# In[35]:


# info function is used to see the information of our data.
data.info


# In[36]:


'''shape function will tell you how many rows and columns are there in our data. Here, 324 rows and 23 
columns are there.'''
data.shape


# In[37]:


"""describe function will give the basic descriptive statistics of our dataset - It will give us the 
basic report which contains the count, mean, std and min columns."""
data.describe()


# In[38]:


# drop_duplicates function is used for dropping the duplicates in our dataset.
data.drop_duplicates()


# In[39]:


'''isnull function checks whether the column or row contains null values or not. If there is null
value, then it will return True, otherwise it will return False.'''
data.isnull()


# In[40]:


""" isnull().sum() will calculate all the null values of the particular column. It will check how many
null values are present in each column. It is basically used for checking how many null values are
there in the particular column."""
data.isnull().sum()


# In[41]:


'''notnull function is the opposite of null function which means it will give True if the values are
not null and it will give False if the values are null.'''
data.notnull()


# In[42]:


# isnull().sum().sum() will tell us how many total null values are there in our dataset.
data.isnull().sum().sum()


# In[43]:


""" Method 1: For Filling the null values in our dataset.
fill null or missing values function. value = 0 means NaN or null values will be replaced by 0. Now 
no null values are present in our dataset."""
data2 = data.fillna(value=0)
data2


# In[44]:


'''Method 1: For Filling the null values in our dataset.
You can type any values like 1 or 2 or 3 in place of NaN or null values. Now no null values are
present in our dataset.'''
data2 = data.fillna(value = 3)
data2


# In[45]:


# isnull().sum().sum() is used to get the total null values in our dataset.
data2.isnull().sum().sum()


# In[46]:


# display or print the entire data of our dataset.
data


# In[47]:


"""Method 2: For Filling the null values in our dataset. (Forward Filling).
Forward Filling means filling null values with the previous value in our dataset."""
# ffill() is equivalent to method='pad'.
data3 = data.ffill()
data3


# In[48]:


"""Method 3: For Filling the null values in our dataset. (Backward Filling).
Backward Filling means filling null values with the next value in our dataset."""
# bfill() is equivalent to method='bfill'.
data4 = data.bfill()
data4


# In[49]:


# numpy library is used for handling our numeric dataset.
import numpy as np


# In[50]:


# matplotlib library is used for plotting purposes like plotting scatter plot, bar plot.
import matplotlib.pyplot as plt


# In[51]:


'''scipy library is a cool library. It contains all the basic functions like statistics functions,
regression functions and more advanced functions.'''
from scipy import stats


# In[52]:


"""We detect the outliers using IQR. Outlier is basically the unwanted data which we don't want in our
dataset."""
data2.columns


# In[53]:


'''IQR will only be visible in the numeric dataset. It is not applicable in the wrong form of the date
format and it is also not applicable in the String formatting.'''
"""Here, we remove the column that contains the String type or Date-Time format. All columns should
contain data only in numeric form."""
# So, Here we drop the 'Oberservation' column in the dataset.
'''axis = 1 is for column, axis = 0 is for row,inplace = True means permanent committing or
permanently delete from our data2, otherwise it will not delete our 'Observation' column.'''
data2.drop(['Observation'], axis = 1, inplace = True)


# In[54]:


# now our 'Observation' column is removed
data2.columns


# In[55]:


"""Now, we will check the outliers by using the IQR. IQR is the Inter-Quartile Range.
Formula for calculating the IQR = Q3 - Q1. Q1 is the Quartile 1, Q2 is the Quartile 2, Q3 is the
Quartile 3, data2 is the dataset. The formula for finding the IQR means the range between which our
dataset has to come, otherwise it will be considered as an outlier."""
# Here, we get the IQR of particular columns
Q1 = data2.quantile(0.25)  # which means 25th percentile to 25th percentile
Q3 = data2.quantile(0.75)  # which means 25th percentile to 75th percentile
IQR = Q3 - Q1  # fixed formula for finding the IQR
'''prints the IQR or Range of that particular column and our dataset has to come in this particular
range, otherwise it will be considered as an outlier and we will have to remove that outlier. It means
from 25th percentile to 75th percentile our dataset has to come in this particular range. The dataset
which comes in this particular range is clean and good for us, otherwise it will be an outlier and we
will have to remove that outlier.'''
print(IQR)


# In[56]:


# For Removing Outliers, here is the particular formula:
"""Formula for Removing Detected Outliers. .any() checks if it is doing in right column or not.
.any() function will check that it will commit or remove the outliers from the proper row. It will
not remove the proper value and will do just for proper checking. axis = 1 means it will do in all
the columns. axis = 0 means it will do in all the rows."""
'''So, here, the data which is less than the 1st range and greater than the 2nd range will be
considered as an outlier and it will be removed from our dataset.'''
data2 = data2[~((data2<(Q1-1.5*IQR)) | (data2>(Q3+1.5*IQR))).any(axis = 1)]
# Our outliers are now removed and this is the clean form of our dataset.
data2


# In[57]:


"""describe means descriptive statistics. This is the proper descriptive statistics of our cleaned
dataset."""
data2.describe()

