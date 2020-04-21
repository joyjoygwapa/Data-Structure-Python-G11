    #Double Linked List by Ethyl Joy I. Badiang
class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class Linked:
    def __init__(self,val):
        self.root=node(val)
        self.current=self.root

    def add(self,item):#adds node
        temp=node(item)
       # print(temp)
        self.current.next=temp
        self.current=self.current.next
        
    def delete(self,node):#deletes node
        start=self.root
        while start.next != node:
            start=start.next
        newloc=node.next
        start.next=newloc
    
    def getval(self,node): #gets value of node
        return node.val
        
    def search(self,val): #searches node
        start=self.root
        if start.next.val!=val:
            start=start.next
            
        if start.next!=val:
            #print('search:',start.next.val)
            return (start.next)
        else:
            print('NONE')
    
    def index(self,index):#displays node value of index
        start=self.root
        for x in range(index-1):
            start=start.next
        print('index:',start.next.val)
        return (start.val)
        
    def display(self): #displays
        print('current:',self.current.val)
        #print('previous:',self.val)
        
    def next (self,node):#determines next value
        print('next:',node.next.val)
        return (node.next)
    def previous(self,val): #displays previous value
        start=self.root
        while start.next!=val:
            start=start.next
        print('previous:',start.val)
        return (start.val)
    
        
        
arr=Linked(0)
arr.add(6)
arr.add(8)
arr.add(10)
arr.next(arr.search(8))
arr.search(7)
arr.index(1)
arr.delete(arr.search(8))
arr.display()
arr.previous(arr.search(8))
