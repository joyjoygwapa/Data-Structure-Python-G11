#Linked List by Ethyl Joy I. Badiang
class disk:
    def __init__(self,file,filename):
        self.file=file
        self.read=self.file
        self.root=filename
        self.arrmain=[]
    def display(self):
        #self.arrmain.append(self.root)
        linked=Linked(self.root)
        for line in self.file:
            x = line.strip()
            arr=''
            for y in line:
                arr=arr+y
                if len(arr)==10:
                    linked.add(arr)
                    arr=''
        
        linked.add(arr) 
        linked.display()
        
        
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
        if start.next.val==val:
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
        print('current:',self.next)
        
    def next (self,node):#determines next value
        print('next:',node.next.val)
        return (node.next)
    

arr=[]
print('BLOCKSISE:10')
print('1---save')
print('2---dalete')
print('3---display')
print('4---terminate')
while True:
    
    choice=int(input('Enter choice:'))
    filename=input('Enter filename:')
    file=open(filename,"r")
    disk=disk(file,filename)
    if choice==1:
        arr.append(filename)
        print(arr)
    elif choice==2:
        name=input('Enter filename:')
        arr.remove(name)
        print(arr)
    elif choice==3:
        disk.display()
    elif choice==4:
        break
    
