
# coding: utf-8

# In[3]:


def compressed(s):
    count=1
    new=[]
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            count+=1
        else:
            new.extend([s[i],str(count)])
            count=1
    return ''.join(new)
        
    
st=input('Enter string: ')
print('Compressed string is: ',compressed(st))

