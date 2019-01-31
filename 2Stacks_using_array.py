
# coding: utf-8

# In[7]:


class _2stacks:
    def __init__(self,n):
        self.size=n
        self.top1=-1
        self.top2=self.size
        self.arr=[None]*n
    
    def push1(self,data):
        if self.top1< self.top2-1:
            self.top1+=1
            self.arr[self.top1]=data
        else:
            print('Stack Overflow')
            
    
    def push2(self,data):
        if self.top2>self.top1+1:
            self.top2-=1
            self.arr[self.top2]=data
        else:
            print('Stack Overflow')
        
    def pop1(self):
        if self.top1>-1 :
            x=self.arr[self.top1]
            self.top1-=1
        else:
            print('Stack empty')
        return x
        
    def pop2(self):
        if self.top2<self.size :
            x=self.arr[self.top2]
            self.top2+=1
        else:
            print('Stack Empty')
        return x
        
    #def printStack(self):
        
    
    
if __name__=='__main__':
    array_stack=_2stacks(6)
    array_stack.push1(2)
    array_stack.push1(1)
    array_stack.push1(3)
    array_stack.push1(8)
    
    array_stack.push2(4)
    array_stack.push2(5)
    
    print('Popped element is {}'.format(array_stack.pop1()))
    print('Popped element is {}'.format(array_stack.pop1()))
    
    print('Popped element is {}'.format(array_stack.pop2()))
    print('Popped element is {}'.format(array_stack.pop2()))
    
    

