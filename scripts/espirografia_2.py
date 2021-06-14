#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import numpy as np
caneta = turtle.Turtle()


# In[14]:


R, r, d = 5, 3, 100
t = np.linspace(0, np.pi, num=50)

caneta.reset()
#hipotrocóide
x = (R - r) * np.cos(t) + d * np.cos(((R + r) / r) * t)
y = (R - r) * np.sin(t) - d * np.sin(((R + r) / r) * t)

for i in range(len(x)):
    caneta.setpos(x[i], y[i])


# In[ ]:




