#Linked List by Ethyl Joy I. Badiang
class disk:
    def __init__(self,filename):
        self.root=filename
        self.arrmain=[]
    def display(self,file,block): #separate text in blocksise
        linked=Linked(self.root)
        
        for line in file:
            x = line.strip()
            arr=''
            for y in line:
                arr=arr+y
                if len(arr)==block:
                    linked.add(arr)#add node
                    arr=''
        linked.add(arr) 
        linked.display()#call display

    def remove(self,arr): #function to remove filename
        for x in range(len(arr)):
            if arr[x]==self.root:#if filename is on the list
                well=True
                break
            else:#if filename is not on the list
                well=False
        if well==True: #remove filename
            arr.remove(self.root)            
        else: #filename not on list
            print('File is not in the list!')
        return arr
        
        
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
        start=self.root
        arr=''
        print('PER NODE:')
        while start.next!=self.current:
            print(start.next.val) #per node
            arr=arr+str(start.next.val)
            start=start.next
        print(self.current.val)
        print ('WHOLE TEXT:')
        arr=arr+str(self.current.val) #whole text
        print(arr)
        
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
    if choice==1:#save filename
        filename=input('Enter filename:')
        arr.append(filename)

    elif choice==2:#delete filename
        filename=input('Enter filename:')
        disks=disk(filename)
        arr=disks.remove(arr)
    elif choice==3:#display file
        filename=input('Enter filename:')
        file=open(filename,"r")
        disks=disk(filename)
        block=int(input('Enter blocksise:'))
        disks.display(file,block)
    elif choice==4:#terminate
        break
    
