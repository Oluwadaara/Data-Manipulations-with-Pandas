#!/usr/bin/env python
# coding: utf-8

#  use the import keyword to include it in your applications

# In[1]:


import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


# Pandas is typically imported using the pd alias

# In[2]:


import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)


# PANDAS SERIES
# What is a Series?
# A Pandas Series is like a column in a table.
# 
# It is a one-dimensional array holding data of any type.

# In[3]:


import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)


# Create Labels
# With the index argument, you can name your own labels.

# In[4]:


import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)


# Series of Key/Value Objects
# When creating a Series, you can also use a key/value object like a dictionary.

# In[5]:


import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)


# DataFrames
# What is a DataFrame, exactly?
# A Pandas DataFrame is a two-dimensional data structure that functions similarly to a two-dimensional array or a table with rows and columns.

# In[6]:


import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)


# How row is located.

# In[7]:


print(myvar.loc[0])


# In[8]:


#use a list of indexes:
print(myvar.loc[[0, 1]])


# Indexes with names

# In[9]:


import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)


# Identify Named Indexes

# In[10]:


#refer to the named index:
print(df.loc["day2"])


# Into a DataFrame, load a comma separated file (CSV file):

# In[11]:


import pandas as pd

df = pd.read_csv('data.csv')

print(df)


# Getting Information about the data

# In[12]:


df.info()


# In[13]:


df.describe()


# JSON could be read into dataframe.

# In[14]:


import pandas as pd

df = pd.read_json('data.js')

print(df) 


# Viewing the Information

# In[15]:


import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))


# In[16]:


print(df.tail()) 


# Information on the Data

# In[17]:


print(df.info())


# Adding new column to existing DataFrame in Pandas
# Method #1: By declaring a new list as a column.

# In[18]:


# Import pandas package 
import pandas as pd
  
# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
display(df)
# Declare a list that is to be converted into a column
location = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
  
# Using 'Address' as the column name
# and equating it to the list
df['Location'] = location
  
# Observe the result
df


# Method #2: By using DataFrame.insert()

# In[19]:


# Using DataFrame.insert() to add a column
df.insert(2, "Age", [21, 23, 24, 21], True)
  
# Observe the result
df


# Working with Missing Data in Pandas

# In[20]:



# importing pandas as pd
import pandas as pd
  
# importing numpy as np
import numpy as np
  
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
  
# creating a dataframe from list
df = pd.DataFrame(dict)
  
# using isnull() function  
df.isnull()


# In[21]:



# importing pandas package 
import pandas as pd 
    
# making data frame from csv file 
data = pd.read_csv("employees.csv") 
    
# creating bool series True for NaN values 
bool_series = pd.isnull(data["Gender"]) 
    
# filtering data 
# displaying data only with Gender = NaN 
data[bool_series]


# In[22]:



# importing pandas as pd
import pandas as pd
  
# importing numpy as np
import numpy as np
  
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
  
# creating a dataframe using dictionary
df = pd.DataFrame(dict)
  
# using notnull() function 
df.notnull()


# In[23]:


# importing pandas package 
import pandas as pd 
    
# making data frame from csv file 
data = pd.read_csv("employees.csv") 
    
# creating bool series True for NaN values 
bool_series = pd.notnull(data["Gender"]) 
    
# filtering data 
# displayind data only with Gender = Not NaN 
data[bool_series]


# Filling missing values using fillna(), replace() and interpolate()

# In[24]:



# importing pandas as pd
import pandas as pd
  
# importing numpy as np
import numpy as np
  
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
  
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
  
# filling missing value using fillna()  
df.fillna(0)


# In[25]:



# importing pandas as pd
import pandas as pd
  
# importing numpy as np
import numpy as np
  
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
  
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
  
# filling a missing value with
# previous ones  
df.fillna(method ='pad')


# In[26]:


# importing pandas package 
import pandas as pd 
    
# making data frame from csv file 
data = pd.read_csv("employees.csv") 
  
# filling a null values using fillna() 
data["Gender"].fillna("No Gender", inplace = True) 
  
data


# In[27]:



# importing pandas package 
import pandas as pd 
    
# making data frame from csv file 
data = pd.read_csv("employees.csv") 
    
# will replace  Nan value in dataframe with value -99  
data.replace(to_replace = np.nan, value = -99)


# Dropping missing values using dropna()

# In[28]:



# importing pandas as pd
import pandas as pd
  
# importing numpy as np
import numpy as np
  
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
  
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
df


# In[29]:


#Dropping rows with at least 1 null value
# using dropna() function 
df.dropna()    


# In[30]:


#Dropping columns with at least 1 null value.
# using dropna() function
df.dropna(axis = 1)


# In[31]:


# dictionary of lists
dict = {'First Score':[100, np.nan, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, np.nan, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
  
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
    
df


# In[32]:


#Dropping rows if all values in that row are missing
# using dropna() function    
df.dropna(how = 'all')


# Dropping Rows with at least 1 null value in CSV file

# In[33]:


# making data frame from csv file 
data = pd.read_csv("employees.csv") 
    
# making new data frame with dropped NA values 
new_data = data.dropna(axis = 0, how ='any') 
    
new_data


# In[34]:


new_data.Team.value_counts()


# In[35]:


new_data = data.rename(columns = {'Team':'Department'})
new_data.head()


# In[36]:


new_data.groupby('Department')
new_data.head()


# importing data from a url or web page

# In[37]:


import pandas as pd
import numpy as np
import urllib.request
url= 'https://raw.githubusercontent.com/leosmigel/analyzingalpha/master/2019-09-30-data-manipulation-with-python/companies.csv'
with urllib.request.urlopen(url) as f:
  companies = pd.read_csv(f, index_col='id')
companies.head()


# In[38]:


sector_group = companies.groupby(by='sector')
print(sector_group)


# aggregation

# In[39]:


print(sector_group.size())
sector_group.size().sum()


# Grouping by multiple columns

# In[40]:


companies.groupby(['sector', 'industry_group'])['employees'].sum()


# I supply a specified function find percent and return the converted series in the example below.

# In[41]:


def find_percent(column):
  return column / float(column.sum())
companies.groupby('sector').agg({'employees': 'sum'}).transform(find_percent)


# In[42]:


companies.groupby('sector').agg({'employees':'sum'}).transform([lambda x: x / x.sum()])


# In[43]:


companies.groupby('sector').apply(lambda x: x['employees'] * 2)


# filtration

# In[44]:


companies.groupby('sector').filter(
    lambda x: x['employees'].sum() > 1000000
    )[['name', 'employees']]


# Pivot Table

# In[45]:


companies.pivot_table(columns='sector', values='employees', aggfunc='sum')


# Joining data

# In[48]:


import pandas as pd
import numpy as np
import urllib.request
url= 'https://raw.githubusercontent.com/leosmigel/analyzingalpha/master/2019-09-30-data-manipulation-with-python/securities.csv'
with urllib.request.urlopen(url) as f:
  securities = pd.read_csv(f, index_col='id')
securities.head()


# In[49]:


securities_companies = companies.join(securities)
securities_companies.head()


# In[ ]:




