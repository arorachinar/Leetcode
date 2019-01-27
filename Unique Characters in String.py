
# coding: utf-8

# In[25]:


#To check if string has unique characters
s=input('Enter the string you want to check')
mylist=[]
check=True
for i in range(len(s)):
    if s[i] in mylist:
        check=False
        print(check)
        break
    else:
        mylist.append(s[i])
if (check):
    print(check)
 

