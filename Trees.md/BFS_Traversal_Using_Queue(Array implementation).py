
# coding: utf-8

# In[13]:


class Treenode:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def BFSTraversal(root):
        queue=[]
        temp=root
        #Printing element at root node
        queue.append(temp)
        while(len(queue)>0):
            print(queue[0].data)
            temp=queue.pop(0)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)

                
    root=Treenode(1)
    root.left=Treenode(2)
    root.right=Treenode(3)
    root.left.left=Treenode(4)
    root.left.right=Treenode(5)
    
    BFSTraversal(root)
    

