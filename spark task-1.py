#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt


# In[6]:


df=pd.read_excel("C:/Users/navolina/Desktop/spark task/task -1/regression.xlsx")


# In[7]:


df


# In[8]:


df.plot(x="Hours",y="Scores",style="*")
plt.xlabel("Study hours")
plt.ylabel("student scores")
plt.title("Study vs Score")
plt.show()


# In[12]:


from scipy import stats 
x=df["Hours"]
y=df["Scores"]

slope,intercept,r,p,std_err =stats.linregress(x,y)

def fun(x):
    return round((slope*x+intercept),3)
c=list(map(fun,x))

plt.plot(x,c)
plt.scatter(x,y)


# In[13]:


result=fun(9.25)
print("Predicted score of a student who study 9.25hrs/day is : ", result)

