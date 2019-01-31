
# coding: utf-8

# In[20]:


class StackNode:
    def __init__(self,data):
        self.data=data
        self.next=None
    
    

class Stack():
    def __init__(self):
        self.head=None
        
    def push(self,data):
        node=StackNode(data)
        node.next=self.head
        self.head=node
    
    def pop(self):
        if self.isEmpty():
            raise Exception('The stack is empty')
        temp=self.head
        self.head=temp.next
        
    def peek(self):
        if self.head is None:
            raise Exception('Stack is Empty')
        else:
            temp=self.head
            return temp.data
    
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    
    def printStack(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
    #def getMin(self):
        
        
        
if __name__=='__main__':
    stack=Stack()
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print('Element at top of stack is: {}'.format(stack.peek())) 
    print('All elements: ')
    stack.printStack()
    
    stack.pop()
    stack.pop()
    stack.pop()
    #stack.pop()
    #stack.pop()
    print('Element at top of stack is: {}'.format(stack.peek()))
    
    print('All elements: ')
    stack.printStack()
    

    

