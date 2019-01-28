
# coding: utf-8

# # Date: 27th January
# 

# In[27]:


#Check if one string is permutation of other
x=input(' Enter First string')
y=input(' Enter second string')

#If we can use in built function sorted 
#if(sorted(x)==sorted(y)):
#     print('Permutations!')
# else:
#     print('Sorry!')

dict={}
c=0
for i in range(len(x)):
    dict.update({x[i]:ord(x[i])})
print(dict)
for j in range(len(y)):
    if dict.get(y[j]) != None:
        c+=1
print(c)
if c==len(x):
    print('Permutation')
else:
    print('Not permutation')


# In[128]:


def permute(str1,str2):
    int_array=[0 for _ in range(128)]
    for char in str1:
        a=ord(char)
        int_array[a]+=1
    #print(int_array)
    for char in str2:
        a=ord(char)
        int_array[a]-=1
        if(int_array[a]<0):
            return False
    return True


x=input(' Enter First string')
y=input(' Enter second string')
permute(x,y)


# In[117]:


#---Different Quesiton---
#Simulation: You have a group of couples that decide to have children until they have their first girl, 
#after which they stop having children. What is the expected gender ratio of the children that are born? 1:1
#What is the expected number of children each couple will have? 2

import random
import numpy as np

li=[]

for i in range(100000):
    count=0
    gender=0 #O is boy, 1 is girl
    while(gender==0):
        gender=random.randint(0,1)
        count+=1
    li.append(count-1)
np.mean(li)
        

