class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
        
    def isempty(self):
        if self.data==None:
            return True
        return False
    
    def append(self,v):
        if self.isempty():
            self.data=v
            return
        # elif self.next==None:
        #     self.next=Node(v)
        # else:
        #     self.next.append(v)
        # Alternative
        temp=self
        while temp.next!=None:
            temp=temp.next
            
        temp.next=Node(v)
        
    
    def insert(self,v):
        if self.isempty():
            self.data=v
            return
        
               
        newnode=Node(v)
        
        self.data,newnode.data=newnode.data,self.data
        self.next,newnode.next=newnode,self.next
        
        
        
    def delete(self,v):
        if self.isempty():
            return
        
        
        if self.data is v:
            if self.next is None:
                self.data=None
            else:
                self.data=self.next.data
                self.next=self.next.next
            return
        
        temp=self       
        while temp.next is not None:
            if temp.next.data is v:
                temp.next=temp.next.next
                return
            temp=temp.next