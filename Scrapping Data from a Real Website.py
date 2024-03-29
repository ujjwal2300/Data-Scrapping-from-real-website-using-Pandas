#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[3]:


print(soup)


# In[4]:


#Find Table 
soup.find('table')


# In[5]:


soup.find_all('table')


# In[6]:


#Table was in second column
soup.find_all('table')[1]


# In[8]:


soup.find('table', class_ ='wikitable sortable')


# In[9]:


table = soup.find_all('table')[1]


# In[10]:


print(table)


# In[16]:


world_titles = table.find_all('th')


# In[17]:


world_titles


# In[18]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[19]:


import pandas as pd


# In[20]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[21]:


column_data = table.find_all('tr')


# In[26]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    
    length = len(df)
    df.loc[length] = individual_row_data 
    


# In[27]:


df


# In[30]:


df.to_csv(r'C:\Users\ujjwal kumar\OneDrive\Web Scrapping\Companies.csv', index=False)


# In[ ]:




