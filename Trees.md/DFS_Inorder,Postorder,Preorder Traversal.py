
# coding: utf-8

# In[13]:


class Treenode:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)
def Preorder(root):
    if root:
        print(root.data)
        Preorder(root.left)
        Preorder(root.right)
    
def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data)
            
root=Treenode(1)
root.left=Treenode(2)
root.right=Treenode(3)
root.left.left=Treenode(4)
root.left.right=Treenode(5)

Inorder(root)
print('-----')
Preorder(root)
print('-----')
Postorder(root)
    
#BFSTraversal(root)

