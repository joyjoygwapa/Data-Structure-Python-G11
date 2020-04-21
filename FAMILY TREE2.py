#Family Tree by Francis Ann Emmanuel G. Arcamo and Ethyl Joy I. Badiang      
class node:
    def __init__(self,val):
        self.val=val
        self.parent=None
        self.node=[]
        
    
class Tree:
    def __init__(self,val):
        self.root=node(val)
        self.current=node(val)


    def add(self,child, parent):#add member
       
        par=self.find(parent)
        if parent ==self.root.val:
            self.current.parent=par
            self.current.node=self.root.node.append(child)
        else:
            self.root=node(parent)
            self.current.parent=par
            self.current.node=self.root.node.append(child)#add child
            self.current.node=self.root.node
        
    def find(self,name):#find parent
        start=self.root
        if name==self.root.val:
            return start.val
        else:
            for x in self.root.node:
                if x==name:
                    return x
                    break
            
                    
    def display(self): #displays
        start=self.root
        print('parent:',self.current.parent)
        print('children:',self.root.node)
        
trees=Tree('Juan')
trees.add("Maria", "Juan")
trees.add("Ethyl", "Juan")
trees.add("Joy", "Juan")
trees.display()
trees.add("Francis", "Maria")
trees.add("Odette", "Maria")
trees.display()
trees.add('Jane','Odette')
trees.display()
trees.add('Ezekiel','Jane')
trees.display()

