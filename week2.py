#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import seaborn as sns




x = np.linspace(0,5, 15)
y = x ** 2

fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.9])

axes.plot(x, y,'b')
axes.set_xlabel('x label')
axes.set_ylabel('y label')
axes.set_title('title')


# In[10]:


fig, axes = plt.subplots()
axes.plot(x,y,'r')
axes.set_xlabel('x label')
axes.set_ylabel('y label')
axes.set_title('title')


# In[24]:


fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes: 
    ax.plot(x,y,'b')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.set_title('title')
    


# In[33]:


fig, axes = plt.subplots(1,3,figsize=(12,4))


axes[0].plot(x ** 2, x, x ** 3)
axes[0].set_title('default axes ranges')

axes[1].plot(x, x ** 2, x , x ** 3)
axes[1].axis('tight')
axes[1].set_title('tight axes')

axes[2].plot(x, x ** 2, x, x ** 3)
axes[2].set_ylim([0,60])
axes[2].set_xlim([2,5])
axes[2].set_title("custom axes range");


# In[ ]:





# In[239]:


job = pd.read_csv('job-market.csv')



       
job = job['Classification']
job = job.dropna()
jobCount = job.value_counts()
job['jobs'] = jobCount









# fig, axes = plt.subplots()
# axes.plot(jobCount[0],jobCount[1],'r')
# axes.set_xlabel('x label')
# axes.set_ylabel('y label')
# axes.set_title('title')


    
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])

# ax.bar(jobCount[1], jobCount[0])

    



# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')

