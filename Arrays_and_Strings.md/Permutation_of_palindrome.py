
# coding: utf-8

# In[22]:



def permute_palin(s):
    arr=[0 for i in range(len(s))]

    for i in range(len(s)):
        arr[i]=s.count(s[i])
    print(arr)
    count=0
    for i in arr:
        if i%2!=0:
            count+=1
    if len(s)%2!=0 and count!=1:
        return False
    elif len(s)%2==0 and count!=0:
        return False

    return True
    

s='Able was I ere I saw Elba'
s=s.replace(' ','')
s=s.lower()
permute_palin(s)

    
        
        
    

