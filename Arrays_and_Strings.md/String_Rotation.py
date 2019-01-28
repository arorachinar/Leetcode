
# coding: utf-8

# In[5]:


s1='foo'
s2='foofoo'
 
def isSubstring(s1,s2):
    if s1.find(s2)!=-1:
        return True
    else:
        return False

def rotateCheck(s1,s2):
    if(len(s1)==len(s2)):
        s1=s1+s1
        #print(s1)
        return isSubstring(s1,s2)
    else:
        return False
rotateCheck(s1,s2)                
                
        

