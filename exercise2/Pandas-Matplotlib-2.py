#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[43]:


age=[24,28,30,35,45,50]
salary_python=[800,1200,1400,1500,1600,2000]


# In[44]:


plt.plot(age,salary_python,color='red',linestyle='--',marker='.')
plt.xlabel('Age')
plt.ylabel('Monthly Salary')


# In[45]:


salary_js=[700,900,1100,1200,1400,1800]
plt.plot(age,salary_js,color='blue',linestyle='-',linewidth=2, marker='o',label='JavaScript')
plt.plot(age,salary_python,color='red',linestyle='--',marker='.',label='Python')
plt.xlabel('Age')
plt.ylabel('Monthly Salary')
plt.legend()


# In[62]:



x_indexes=np.arange(len(age))
width=0.7

plt.bar(x_indexes+width,salary_js,color='blue',width=width)
plt.xticks(range(7), ['0','25','30','35','40','45','50'], fontsize=8, rotation=90)


# In[ ]:




