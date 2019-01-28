
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
 


# In[12]:


#Assuming ASCII character set
#Returns true if all characters are unique, else returns False.

def isunique(str):
    if(len(str)>128):
        return False
    char_bool=[False for _ in range(128)]
    for char in str:
        #Get ASCII code for character
        a=ord(char)
        if(char_bool[a]):
            return False
        char_bool[a]=True
        
    return True
        
st=input('Enter the string')
isunique(st)
            
        


# In[10]:




