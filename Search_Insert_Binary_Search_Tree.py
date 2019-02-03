
# coding: utf-8

# In[85]:


class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
   
    def insert(self,nod):
        
        if self is None:
            self=nod
        else:
            if self.data>nod.data:
                if self.right is None:
                       self.right=nod
                else:
                    self.right.insert(nod)
            if self.data<nod.data:
                if self.left is None:
                    self.left=nod
                else:
                    self.left.insert(nod)
    
    def inorderPrint(self):
        if self:
            inorderPrint(self.left)
            print(self.data)
            inorderPrint(self.right)
        
    
    def search(self,key):
        #print('Hey')
        if key>self.data:
            if self.right is None:
                return('Not found')
            return self.right.search(key)
        elif key<self.data:
            if self.left is None:
                return('Not found')
            return self.left.search(key)
        else:
            return('Value found')
    
no=node(8)
no.left=node(3)
no.right=node(10)
no.left.left=node(1)
no.left.right=node(6)
no.left.right.left=node(4)
no.left.right.right=node(7)
no.right.right=node(14)
    
print(no.search(8))
print(no.search(90))

no.insert(node(9))

inorderPrint(no)

