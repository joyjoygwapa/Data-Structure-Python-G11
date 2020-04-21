        
class node:
    def __init__(self,val):
        self.val=val
        self.node=[]
        self.below=None 

class Tree:
    def __init__(self,val):
        self.root=node(val)
        self.current = self.root
        self.parent=[]
    def add(self,child, parent):
        par     = self.find(parent)
        self.par = par
        self.current = self.next.append(child)
        while self.current.next!=None:
            self.current = self.next
        self.current.next= node(child)
        self.current=self.current.next
##        print('self.current:',self.current.val)
##        self.parent.append(self.current)
        
    def find(self,name):
        start = self.root
        while start.val!=name:
            start=start.next
        return start
    
    def display(self): #displays
        start=self.root

        while start!=None:
            print (start.val)
            start=start.next

trees=Tree('Juan')
trees.add("Maria", "Juan")
trees.add("Ethyl", "Maria")
trees.add("Joy", "Maria")
trees.add("Francis", "Juan")
trees.add("Odette", "Maria")
##trees.add('Jane','Odette')
##trees.add("James","Ethyl")

trees.display()
print ('cc',trees.find("Ethyl").val)
