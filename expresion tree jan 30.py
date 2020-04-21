class node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
class Trees:
    def __init__(self,prob):
        self.left=None
        self.right=None
        self.exp=prob
        
        
        
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
    def tree(self):
        arr=[]
        for x in self.exp:
            
            if sign(x)!=True:
                key=node(x)
                arr.append(key)
            else :
                key=node(x)
                key1=arr.pop()
                key2=arr.pop()

                key.right=key1
                key.left=key2
                arr.append(key)
        key=arr.pop()
##        print(key.val)
        return key

def sign(char):
    if char=='+' or char=='-' or char=='/' or char=='*' or char=='^' :
        return True
    else:
        return False
    


prob=input('Enter problem:')
trees=Trees(prob)
sol=trees.tree()
trees.inOrder(sol)
##print(trees.left)

