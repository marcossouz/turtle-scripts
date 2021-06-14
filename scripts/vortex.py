#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
pen = turtle.Turtle()


# In[2]:


def circle(r):
    pen.pensize(1.5)
    pen.pu()
    pen.rt(90)
    pen.fd(r)
    pen.lt(90)
    pen.pd()
    pen.circle(r)


# In[3]:


def center():
    pen.pu()
    pen.setpos(0.0, 0.0)
    pen.pd()


# In[4]:


def marcacao(r):
    pen.lt(50)
    for i in range(9):
        center()
        pen.pu()
        pen.fd(r+25)
        pen.write(f"{i+1}", font=("Arial", 16, "normal"))
        pen.rt(40)
    pen.rt(50)
    center()


# In[5]:


def pontos(r):
    pen.shape('circle')
    pen.shapesize(0.3, 0.3, 0.3)
    pen.lt(50)
    for i in range(9):
        center()
        pen.pu()
        pen.fd(r)
        pen.stamp()
        pen.rt(40)
    pen.rt(50)
    center()
    pen.shape('classic')
    pen.shapesize(1, 1, 1)


# In[6]:


# positions
# 1 -> (128.56, 153.21)
# 2 -> (196.96, 34.73)
# 3 -> (173.21, -100.00)
# 4 -> (68.56, -187.94)
# 5 -> (-68.56, -187.94)
# 6 -> (-173.21, -100.00)
# 7 -> (-196.96, 34.73)
# 8 -> (-128.56, 153.21)
# 9 -> (0.00, 200.00)

# angulos
# 1 -> lt(50)
# 2 -> lt(10)
# 3 -> rt(30)
# 4 -> rt(70)
# 5 -> rt(110)
# 6 -> rt(150)
# 7 -> rt(180)
# 8 -> lt(130)
# 9 -> lt(90)


# In[6]:


def trace(n):
    if n == '1':
        pen.up()
        pen.lt(50)
        pen.fd(200)
        pen.pd()
#         pen.rt(50)
    elif n == '2':
        pen.up()
        pen.lt(10)
        pen.fd(200)
        pen.pd()
#         pen.rt(10)
    elif n == '3':
        pen.up()
        pen.rt(30)
        pen.fd(200)
        pen.pd()
#         pen.lt(30)
    elif n == '4':
        pen.up()
        pen.rt(70)
        pen.fd(200)
        pen.pd()
#         pen.lt(70)
    elif n == '5':
        pen.up()
        pen.rt(110)
        pen.fd(200)
        pen.pd()
#         pen.lt(110)
    elif n == '6':
        pen.up()
        pen.rt(150)
        pen.fd(200)
        pen.pd()
#         pen.lt(150)
    elif n == '7':
        pen.up()
        pen.rt(190)
        pen.fd(200)
        pen.pd()
#         pen.lt(190)
    elif n == '8':
        pen.up()
        pen.lt(130)
        pen.fd(200)
        pen.pd()
#         pen.rt(130)
    elif n == '9':
        pen.up()
        pen.lt(90)
        pen.fd(200)
        pen.pd()
#         pen.rt(90)
    elif n == '012' or n == '023' or n == '034'         or n == '045' or n == '056' or n == '067'         or n == '078' or n == '089' or n == '091':
        pen.rt(110)
        pen.fd(135)
    elif n == '123' or n == '234' or n == '345'         or n == '456' or n == '567' or n == '678'         or n == '789' or n == '891' or n == '912':
        pen.rt(40)
        pen.fd(135)
    elif n == '024' or n == '035' or n == '046'         or n == '057' or n == '081' or n == '092' or n == '013':
        pen.rt(130)
        pen.fd(260)
    elif n == '124' or n == '235' or n == '346'         or n == '457' or n == '568' or n == '679'         or n == '781' or n == '892' or n == '913':
        pen.rt(60)
        pen.fd(260)
    elif n == '135' or n == '246' or n == '357'         or n == '468' or n == '579' or n == '681'         or n == '792' or n == '813' or n == '924':
        pen.rt(80)
        pen.fd(260)
    elif n == '134' or n == '245' or n == '356'         or n == '467' or n == '578' or n == '689'         or n == '791' or n == '812' or n == '923':
        pen.rt(60)
        pen.fd(135)
    elif n == '137' or n == '248' or n == '359'         or n == '461' or n == '572' or n == '683'         or n == '794' or n == '815' or n == '926':
        pen.rt(120)
        pen.fd(396)
    elif n == '154' or n == '265' or n == '376'         or n == '487' or n == '598' or n == '619'         or n == '721' or n == '832' or n == '943':
        pen.lt(120)
        pen.fd(135)
    elif n == '167' or n == '278' or n == '389'         or n == '491' or n == '512' or n == '623'         or n == '734' or n == '845' or n == '956':
        pen.rt(120)
        pen.fd(135)
    elif n == '197' or n == '218' or n == '329'         or n == '431' or n == '542' or n == '653'         or n == '764' or n == '875' or n == '986':
        pen.lt(60)
        pen.fd(260)
    elif n == '184' or n == '295' or n == '316'         or n == '427' or n == '538' or n == '649'         or n == '751' or n == '862' or n == '973':
        pen.lt(120)
        pen.fd(396)
#     center()


# In[7]:


def vortex(n):
    r = 200
    pen.reset()
    center()
    circle(r)
    marcacao(r)
    pontos(r)
    trace('2')
    
    a = '0'
    b = '2'
    c = '4'
    
    for _ in range(n):              
        if(int(c) > 9):
            aux = 0
            for i in c:
                aux += int(i)
            c = str(aux)
        
        trace(f'{a}{b}{c}')
#         print(a, b, c)
        
        a = b
        b = c
        c = str(int(c) + int(c))


# In[8]:


vortex(10)


# In[ ]:




