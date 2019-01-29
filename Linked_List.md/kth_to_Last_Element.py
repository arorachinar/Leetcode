
# coding: utf-8

# In[20]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    #Add element to the beggining
    def push(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
    
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
        
    def ktoLast(self,k):
        count=1
        temp=self.head
        while(count!=k):
            count+=1
            temp=temp.next

        while(temp):
            print(temp.data)
            temp=temp.next

        

if __name__=='__main__':
    llist=LinkedList()
    llist.push(34)
    llist.push(45)
    llist.push(56)
    llist.push(67)
    llist.push(78)
    
    llist.printList()
    x=input('Enter k: ')
    llist.ktoLast(int(x))
    

