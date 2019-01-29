
# coding: utf-8

# In[51]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
    
    def push(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
        
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    
    #Complexity O(n) time, N is the size of the linked list
    #Here you're creating a new list traversing the set. 
    #There can be a more efficient of doing this
    
    def removedupl(self):
        current = self.head
        prev=current
        seen = set()
        while current.next!=None:
            if current.data in seen:
                prev.next=current.next
            else:
                seen.add(current.data)
                prev=current
            current=current.next
                
                
#     def removeDuplicatesInplace(self):
#         current=self.head
#         while(current!=None):
#             runner=current
#             prev=current
#             while(runner.next!=None):
#                 if(runner.next.data==current.data):
#                     #prev.next=runner.next
#                     prev.next=runner
#                     runner=runner.next.next
                    
                    
#                 else:
#                     #prev=runner
#                     runner=runner.next
#                 prev=runner
#             current=current.next
        



        
if __name__=='__main__':
    llist=LinkedList()
    
    llist.push(23)
    llist.push(34)
    llist.push(45)
    llist.push(13)
    llist.push(34)
    llist.push(34)
    llist.push(34)
    llist.push(13)
    print('Before Duplicate removal: ')
    llist.printList()
    
    print('After Duplicate removal: ')
    
    llist.removedupl()
    llist.printList()

#     print('Dupilcate removal without temporary buffer: ')
    
#     llist.push(23)
#     llist.push(34)
#     llist.push(45)
#     llist.push(13)
#     llist.push(34)
#     llist.push(34)
#     llist.push(34)
#     llist.push(13)
#     print('Before Duplicate removal: ')
#     llist.printList()
    
#     print('After Duplicate removal: ')
    
#     llist.printList()


# In[17]:


# l=[12,3,5,6,5,6,3,12,12,3]
# s=set()
# for i in l:
#     s.add(i)
# for i in s:
#     print(i,l.count(i))

