#binary tree search by Ethyl Joy I. Badiang
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
    def height(self):
        if self.y>=self.x:
            print('height:',self.y)
        elif self.x>=self.y:
            print('height:',self.x)

    def search(self,num):
        start=self.root
        if num==start.val:
            return self
        elif num<=start.left.val:
            if start.left is None:
                return None
            else:
                
                return num
        elif num>=start.right.val:
            if start.right is None:
                return None
            else:
                return val
                #return start.right.search(num)
    def least(self,cur):
        current=cur
        while current.left!=None:
            current=current.left
        return current
            
    def delete(self,root,num):
        #num=self.search(num)
        start=root
        if start==None:
            print('The numebr is not on the list')
            return root

       
        if num<start.val :#put root to leftmost
            start.left=self.delete(start.left,num)
            
        elif num>start.val :#put root to right most

            start.right=self.delete(start.right,num)

        else:

            if start.left is None:
                cur=start.right
                start=None
                return cur
            elif start.right is None:
                cur=start.left
                start=None
                return cur
        
    

        cur=self.least(start.right)#get new root
        start.val=cur.val#assign new root
        start.right=self.delete(start.right,start.val)#assign values
    

        return start

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
    def height(self):
        x=max(self.arrx)
        y=max(self.arry)
        if y>=x:
            print('height:',y)
        else:
            print('height:',x)

class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


root=50    
binary=Binary(50)
binary.insert(25)
binary.insert(12)
binary.insert(43)
binary.insert(65)
binary.insert(89)
binary.insert(10)
binary.insert(8)
binary.insert(6)
trees=Trees()
print('Pre order')
trees.preOrder(binary.root,1,1)
trees.height()
root=binary.delete(binary.root,50)
print('delete:50')
print('In order')
trees.inOrder(root)


#print('Post order')    
#trees.postOrder(binary.root)

#trees.inOrder(binary.root)
#display(x,y)
#binary.height()
#binary.delete(25)

