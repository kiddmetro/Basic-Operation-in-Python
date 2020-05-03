#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#IGWE CLINTON DONALD
#BHU/19/04/05/0003
#Level 100
#CMP 104


# In[1]:


#(1)
#Area of a Square
#Length of the sides is a
a = int(input("Enter Number for a = "))
Area = a**2
print(Area)


# In[2]:


#(2)
#Area of Rectangle
#l is Length and b is Breadth
l = int(input(" Enter Number for l = "))
b = int(input(" Enter Number for b = "))
Area = l*b
print(Area)


# In[3]:


#(3)
#Area of Triangle
# b is the base of triangle
# h is the height of triangle
b = int(input(" Enter Number for b = "))
h = int(input(" Enter Number for h = "))
Area = 1/2*b*h
print(Area)


# In[4]:


#(4)
#Area of Trapezoid
#b1 & b2 are the bases of the Trapezoid
#h is the height of the Trapezoid 
b1 = int(input(" Enter Number for b1 = "))
b2 = int(input(" Enter Number for b2 = "))
h = int(input(" Enter Number for h = "))
Area = 1/2*(b1 + b2)*h
print(Area)


# In[5]:


#(5)
#Area of a circle
#where Pi is 22/7
# r is the radius
Pi = 22/7
r = int(input(" Enter Number for r = "))
Area = Pi*r**2
print(Area)


# In[6]:


#(6)
#Circumference of a circle
#where Pi is 22/7
# r is the radius
Pi = 22/7
r =  int(input(" Enter Number for r = "))
Circumference = 2*Pi*r
print(Circumference)


# In[7]:


#(7)
#Surface Area of a Cube = S = 6a2
# a is the Length of the sides of a Cube
a = int(input(" Enter Number for a = "))
Area = 6*a**2
print(Area)


# In[8]:


#(8)
#Curved surface area of a Cylinder = 2πrh
#where Pi is 22/7
# r is the radius
# h is the height
Pi = 22/7
r = int(input(" Enter Number for r = "))
h = int(input(" Enter Number for h = "))
Area = 2*Pi*r*h
print(Area)


# In[9]:


#(9)
#Total surface area of a Cylinder 
#where Pi is 22/7
# r is the radius
# h is the height
import math

r = int(input("Enter Number for r = "))
h = int(input("Enter Number for h = "))
Area = 2 * math.pi * r * (r + h)
print(Area)


# In[23]:


#(10)
#Volume of a Cylinder = V = πr2h
#where Pi is 22/7
# r is the radius
# h is the height
Pi = 22/7
r = int(input("Enter Number for r = "))
h = int(input("Enter Number for h = "))
Volume = Pi*r*2*h
print(Volume)


# In[24]:


#(11)
#Acceleration Formula (v-u)/t 
#v is final velocity 
# u is initial velocity
#t is time
v = int(input("Enter Number for v = "))
u = int(input("Enter Number for u = "))
t = int(input("Enter Number for t = "))
Acceleration = (v-u)/t
print(Acceleration)


# In[27]:


#(12)
#density
#m is mass 
#v is volume
m = int(input("Enter Number for m = "))
v = int(input("Enter Number for v = "))
density = m/v
print(density)


# In[30]:


#(13)
#pressure P=F/A 
#where F is force applied 
#A is total area of the object
F = int(input("Enter Number for F = "))
A = int(input("Enter Number for A = "))
Pressure = F/A
print(Pressure)


# In[31]:


#(14)
#kinetic energy is E
#m is mass 
#v is volume
m = int(input("Enter Number for m = "))
v = int(input("Enter Number for v = "))
E = 1/2*m*v**2
print(E)


# In[32]:


#(15)
#V is for voltageV = IR
#I is current and R is resistance in ohms
I = int(input("Enter Number for I = "))
R = int(input("Enter Number for R = "))
V = I*R
print(V)


# In[ ]:




