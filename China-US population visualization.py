#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Using pandas and pyplot to manipulate and show data.


# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[ ]:


#Just a simple test graph


# In[9]:


x = [1, 2, 3]
y = [1 ,4, 9]
z = [10, 5, 0]
plt.plot(x, y)
plt.plot(x, z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y", "this is z"])
plt.show()


# In[ ]:


#Reading in some sample data, then creating a table and graph from it.


# In[11]:


sample_data = pd.read_csv('sample_data.csv')


# In[12]:


sample_data


# In[13]:


type(sample_data)


# In[15]:


sample_data.column_c


# In[19]:


plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.xlabel("x")
plt.show()


# In[ ]:


#Reading in the data of the US and Chinese population.


# In[20]:


data = pd.read_csv('countries.csv')


# In[23]:


data.country == 'United States'


# In[24]:


China = data[data.country == 'China']


# In[25]:


data.country == 'China'


# In[ ]:


#Plotting the data and using division to get a smaller number.


# In[35]:


plt.plot(us.year, us.population / 10**7)
plt.plot(China.year, China.population / 10**7)
plt.show()


# In[36]:


us.population


# In[38]:


us.population / us.population.iloc[0] * 100


# In[ ]:


#Finishing the graph to show the comparison between the two population growths over the years.


# In[39]:


plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(China.year, China.population / China.population.iloc[0] * 100)
plt.legend(['US', 'CHINA'])
plt.xlabel('year')
plt.ylabel('population growth(first year = 100)')
plt.show()

