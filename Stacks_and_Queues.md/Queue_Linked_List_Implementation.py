
# coding: utf-8

# In[3]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.rear=self.front=None
        
    def isEmpty(self):
        return self.front==None
    
    def Enqueue(self,data):
        node=Node(data)
        
        if self.rear==None:
            self.rear=self.front=node
            return
        self.rear.next=node
        self.rear=node
        
    def Dequeue(self):
        if self.isEmpty():
            return
        self.front=self.front.next
        if self.front==None:
            self.rear=None
    
    def printQueue(self):
        temp=self.front
        while(temp):
            print(temp.data)
            temp=temp.next
        
        
if __name__=='__main__':
    q=Queue()
    q.Enqueue(2)
    q.Enqueue(3)
    q.Enqueue(4)
    q.Enqueue(5)
    
    q.Dequeue()
    q.Dequeue()
    
    q.printQueue()

