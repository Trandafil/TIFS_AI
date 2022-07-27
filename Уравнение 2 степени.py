#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Введите номинал банкноты:"))
if n ==1:
    print("Джордж Вашингтон")
elif n ==2:
    print("Томас Джефферсон")
elif n ==5:
    print("Авраам Линкольн")
elif n ==10:
    print("Александр Гамельтон")
elif n ==20:
    print("Эндрю Джексон")
elif n ==50:
    print("Улис Грант")
elif n ==100:
    print("Бенджамин Франклин")
else:
    print("Такой банкноты в США не существует")


# In[4]:


import math
a = float(input("Введите коэфициент а:"))
b = float(input("Введите коэфициент b:"))
c = float(input("Введите коэфициент c:"))
D = b*2-4*a*c
if D<0:
    print("Уравнение не имеет решение на множестве действительных чисел")
elif D == 0:
    x = -b/(2*a)
    print("x = ",x)
else:
    x1 =(-b-math.sqrt(D))/(2*a)
    x2 =(-b+math.sqrt(D))/(2*a)
    print(x1)
    print(x2)


# In[ ]:




