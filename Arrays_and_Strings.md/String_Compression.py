
# coding: utf-8

# In[10]:


def compressed(st):
    s=[]
    st=sorted(st)
    for char in st:
        if(char not in s): 
            s.append(char)
            s.append(st.count(char))
    comp=''
    for i in s:
        comp+=str(i)
    if(len(comp)<len(st)):
        return comp
    else:
        return st
        
    
st=input('Enter string: ')
print('Compressed string is: ',compressed(st))

