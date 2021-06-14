#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import random


# In[2]:


# competidores
alex = turtle.Turtle()
blex = turtle.Turtle()
clex = turtle.Turtle()

# juiz
juiz = turtle.Turtle()


# In[3]:


#numero de passos
passos = 200


# In[4]:


# config juiz
juiz.pu()
juiz.setpos(200, 100)
juiz.rt(90)
juiz.pd()
juiz.fd(200)
juiz.rt(180)


# In[5]:


#reset()
alex.reset()
blex.reset()
clex.reset()

#contadores
n_venc = 0
alex_passos = 0
blex_passos = 0
clex_passos = 0


# In[6]:


#posionando os competidores
alex.pu()
alex.setpos(0, 50)
alex.pd()

clex.pu()
clex.setpos(0, -50)
clex.pd()


# In[7]:


#colors
alex.color('green')
blex.color('blue')
clex.color('red')


# In[8]:


#aparencia
alex.shape('turtle')
blex.shape('turtle')
clex.shape('turtle')


# In[9]:


#largura da linha
alex.pensize(5)
blex.pensize(5)
clex.pensize(5)


# In[10]:


#inicia a corrida
random.seed()
while True:
    # movimenta alex
    k = random.randrange(5)
    alex.fd(k)
    alex_passos += k
    if alex_passos >= passos:
        print("alex venceu a corrida")
        n_venc += 1
        
    k = random.randrange(5)
    blex.fd(k)
    blex_passos += k
    if blex_passos >= passos:
        print("blex venceu a corrida")
        n_venc += 1
        
    k = random.randrange(5)
    clex.fd(k)
    clex_passos += k
    if clex_passos >= passos:
        print("clex venceu a corrida")
        n_venc += 1
        
    if (n_venc > 0): 
        break
        

#temos um ou mais vencedores
if (n_venc == 1):
    print("temos um vencedor")
else: 
    print("houve empate")


# In[ ]:




