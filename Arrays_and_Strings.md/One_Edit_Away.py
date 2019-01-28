
# coding: utf-8

# In[40]:


def oneAway(st1,st2):
    l1=[False for i in range(len(st1))]
    l2=[False for i in range(len(st2))]
    if len(st1)==len(st2):
        count=0
        for i in range(len(st1)):
            if st1[i]!=st2[i]:
                count+=1
        if(count>1):
            return False
    elif abs(len(st1)-len(st2))>1:
        return False
    elif (st1=='' and st2!='') or(st1!='' and st2=='') :
        return True
    
    else:
        if(len(st2)>len(st1)):
            temp=st1
            st1=st2
            st2=temp
        index1=0
        index2=0
        firstDiff=False
        while(index1<len(st1) and index2<len(st2)):
            
            if st1[index1]!=st2[index2]:
                if len(st1)==1:
                    return False
                if firstDiff:
                    return False
                index1+=1
                firstDiff=True
            else:
                index1+=1
                index2+=1
               
                
                
    return True


st1=input('First string')
st2=input('Second string')

oneAway(st1,st2)
    

