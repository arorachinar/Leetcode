
# coding: utf-8

# In[27]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    #Insert node at first position    
    def push(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
        
    #Push elements in LinkedList
    def append(self,data):  
        node=Node(data)
        if(self.head is None):
            self.head=node
            return
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node
        
        
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    #When lengths are equal        
    def printSum(self,llist2):
        temp=self.head
        temp1=llist2.head
        carry=0
        si=0
        sumList=LinkedList()
        while(temp or temp1):
            si=temp.data+temp1.data+carry
            result=si%10
            sumList.append(result)
            carry=si//10
            temp=temp.next
            temp1=temp1.next
        sumList.printList()
                
    def alternateLeetcode(self,list2):
        l1=self.head
        l2=list2.head
        s1=""
        s2=""
        while l1:
            s1+=str(l1.data)
            l1=l1.next
        while l2:
            s2+=str(l2.data)
            l2=l2.next
        s1=s1[::-1]
        s2=s2[::-1]
        #print(s1,s2)
        
        sum=int(s1)+int(s2)
        #print(sum)
        s=str(sum)
        ans=s[::-1]
        #print(ans)
        anslis=[]
        for char in ans:
            anslis.append(int(char))
     
        return anslis
        
        
if __name__=='__main__':
    llist1=LinkedList()
    llist1.append(2)
    llist1.append(1)
    llist1.append(4)
   # llist1.append(6)
    llist1.printList()
    print('-----')
    llist2=LinkedList()
    llist2.append(9)
    llist2.append(0)
    llist2.append(8)
    llist2.printList()
    #print('-----')
    #llist1.printSum(llist2)
    
    print('-----')
    print(llist1.alternateLeetcode(llist2))

