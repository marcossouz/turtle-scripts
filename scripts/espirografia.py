#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[8]:


t = np.linspace(-2, 2, num=10000)
x = t
y = t ** 2

plt.plot(x, y)


# In[11]:


t = np.linspace(0, np.pi, num=10000)
x = t
y = np.cos(t)

plt.plot(x, y)


# In[42]:


# Hypotrochoid
# R, r, d = 5, 3, 5
R, r, d = 1024*1024*1024, 28, 1024*1024*1024
t = np.linspace(0, 10000, 3000)
x = (R - r) * np.cos(t) + d * np.cos(((R - r) / r) * t)
y = (R - r) * np.sin(t) - d * np.sin(((R - r) / r) * t)
plt.figure(figsize=(15, 15))
plt.plot(x, y, linewidth=.05)


# In[26]:


# Hypocycloid
R, r, d = 16, 1024*4, 16
t = np.linspace(0, 1024, 1024*3)
x = (R - r) * np.cos(t) + r * np.cos(((R - r) / r) * t)
y = (R - r) * np.sin(t) - r * np.sin(((R - r) / r) * t)
plt.figure(figsize=(12, 12))
plt.plot(x, y, linewidth=.5)


# In[5]:


# Epicycloid
R, r = 256, 16
t = np.linspace(0, 32, 1024*2)
x = (R + r) * np.cos(t) - r * np.cos(((R + r) / r) * t)
y = (R + r) * np.sin(t) - r * np.sin(((R + r) / r) * t)
plt.figure(figsize=(12, 12))
plt.plot(x, y, linewidth=.5)


# In[27]:


# Epitrochoid
R, r, d = 612, 256, 512
t = np.linspace(0, 1024, 1024*1024)
x = (R + r) * np.cos(t) - d * np.cos(((R + r) / r) * t)
y = (R + r) * np.sin(t) - d * np.sin(((R + r) / r) * t)
plt.figure(figsize=(12, 12))
plt.plot(x, y, linewidth=.5)


# In[ ]:




