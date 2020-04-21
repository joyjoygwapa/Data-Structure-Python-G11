#AVL by Ethyl Joy I. Badiang
class node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
class Trees:
    def __init__(self):
        self.arrx=[]
        self.arry=[]
        
        
    def preOrder(self,n,x,y):#Print the node's data.Then traverse and right subtree.
        if n==None:
            
            return
        print(n.val)
        self.preOrder(n.left,x+1,y)
        self.arrx.append(x)
        self.preOrder(n.right,x,y+1)
        self.arry.append(y)
    def inOrder(self,n): #When you get to a node: Traverse its left subtree. 
                    #Then print the node's data. 
                    #Then traverse its right subtree.
        if n==None:
            return
        self.inOrder(n.left)
        print(n.val)
        self.inOrder(n.right)
    def postOrder(self,n):#When you get to a node: Traverse its left subtree.
                    #Then traverse its right subtree. 
                    #Then print the node's data. 
        if n==None:
            return
        self.postOrder(n.left)
        self.postOrder(n.right) 
        print(n.val)

class Binary:
    def __init__(self, val):
        self.root=node(val)
        self.right=None
        self.left=None
    def insert(self,val):#adds node
        start=self.root
        #temp=node(val)
        while True:
            if start.val>val and start.left==None:
                    temp=node(val)
                    start.left=temp
                    break
            elif start.val<val and start.right==None:
                    temp=node(val)
                    start.right=temp
                    break
            elif start.val<val and start.right!=None:
                    start=start.right
            elif start.val>val and start.left!=None:
                    start=start.left
            elif start.val==val:
                break
    def avl(self,n):
        start=self.root
trees=Trees()
binary=Binary(50)
binary.insert(25)
binary.insert(12)
binary.insert(43)
binary.insert(65)
binary.insert(89)
binary.insert(10)
trees.inOrder(binary.root)
