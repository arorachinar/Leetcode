
# coding: utf-8

# In[16]:


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
        while(temp):
            print(temp.data)
            temp=temp.next
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


# In[10]:


#Leetcode solution. It's the same

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        
        """
        :type head: ListNode
        :rtype: bool
        """
        
#         temp=head
#         ans=""
#         while temp:
#             a=abs(temp.val)
#             #print(a)
#             ans+=str(a)
#             temp=temp.next
        
#         if ans[::-1]==ans:
#             return True
#         else:
#             return False
        
        temp=head
        count=0
        head2=None
        #print(type(head))
        while(temp):
            node=ListNode(temp.val)
            node.next=head2
            head2=node
            temp=temp.next
            
        temp=head
        temp2=head2

        while(temp and temp2):
            if (temp.val!=temp2.val):
                return False
            temp=temp.next
            temp2=temp2.next
        return True
            
                
                
                
            
        
        

