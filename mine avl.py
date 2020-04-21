#AVL TREE by Badiang
class node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.key=val
        
class AVL:
    def __init__(self,val):
        self.key=node(val) 
##        self.key=val
        self.left=None
        self.right=None
        self.height=1

    def height(self): #measure height
        if not self.left:
            if not self.right:
                return 1
            else:
                return 1+self.right.height
        else:
            if not self.right:
                return 1+self.left.height
            else:
                return max(self.left.height,self.right.height)+1
            
    def rightrotate(self): #rotate to right
        n=self.left
        self.left=n.right
        n.right=self
        self=n
        self.right.height()
        self.height()
        return self
    def leftrotate(self): #rotate to left
        n=self.right
        self.right=n.right
        self=n
        self.left.height()
        self.height()
        return self
    def doubler(self): #rotate twice
        self.left=self.left.leftrotate()
        self=self.rightrotate()
        return self
    def doublel(self): #rotate twce
        self.right=self.right.rightrotate()
        self=self.leftrotate()
        return self
    def balance(self): #to determine if balanced
        if not self.left:
            if not self.right:
                return 0
            else:
                self.right.height
        else:
            if not self.right:
                return self.left.height
            else:
                return self.left.height-self.right.height
    def add(self,val):
        if val<self.key.key:
##            print(self.left)
            if not self.left:
                self.left=AVL(val)
            else:
                self.left=self.left.add(val)
                if self.balance()==2:
                    if self.left.balance()==1:
                        self=self.rightrotate()
                    else:
                        self=self.doubler()
        elif val>self.key.key:
            if not self.right:
                self.right=AVL(val)
            else:
                self.right=self.right.add(val)
                if self.balance()==-2:
                    if self.right.balance()==-1:
                        self=self.leftrotate()
                    else:
                        self=self.doublel()
        else:
            print('ALREADY EXISTS')
            self.height=self.height()
        return self
    def inOrder(self): #When you get to a node: Traverse its left subtree. 
                    #Then print the node's data. 
                    #Then traverse its right subtree.
        if self.left:
            self.left.inOrder()
        print(self.key.key)
        if self.right:
            self.right.inOrder()
        
        


avl=AVL(50)
avl.add(17)
avl.add(72)
avl.add(23)
avl.add(19)
avl.add(12)
avl.add(54)
avl.add(76)
avl.inOrder()
##print(avl.key.val)
##avl.inOrder(avl.key)

            
        
        
        
