
# coding: utf-8

# In[20]:


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def append(self,val):
        temp=self.head
        head=None
        while(temp):
            node=Node(val)
            node.next=head
            head=node
            temp=temp.next
            
        
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    #Approach 2        
    def palindrome(self):
        slow=fast=self.head
        stack=[]
        while fast and fast.next:
            stack.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        
        if fast:
            slow=slow.next
        
        while slow:
            top=stack.pop()
            if top!=slow.val:
                return False
            slow=slow.next
        return True
    
    #Approach 1    
    def isPalindrome(self):

        temp=self.head
        head2=None
        #print(type(head))
        while(temp):
            node=Node(temp.val)
            node.next=head2
            head2=node
            temp=temp.next
            
        temp=self.head
        temp2=head2

        while(temp and temp2):
            if (temp.val!=temp2.val):
                return False
            temp=temp.next
            temp2=temp2.next
        return True
    
if __name__=='__main__':
    llist1=LinkedList()
    llist1.append(1)
    llist1.append(2)
    llist1.append(1)
    print(llist1.isPalindrome())
    print(llist1.palindrome())

