class Queue:
    def __init__(self):
        self.queue=[]
        
    def __str__(self):
        return str(self.queue)
        
    def addq(self,v):
        self.queue.append(v)
        
    def isempty(self):
        return self.queue==[]
    
    def deq(self):
        v=None
        if not self.isempty():
            v=self.queue[0]
            self.queue=self.queue[1:]
        return v
 

def neighbours(AMat,v):
    nbrs=[]
    rows,cols=AMat.shape
    for i in range(rows):
        if AMat[v,i]==1:
            nbrs.append(i)
    return nbrs
   
    
def BFS(AMat,v):
    rows,cols=AMat.shape
    visited={}
    for i in range(rows):
        visited[i]=False 
    q=Queue
    
    
    visited[v]=True
    q.addq(v)
    
    while not q.isempty():
        j=q.deq()
        for k in neighbours(AMat,j):
            if not visited[k]:
                visited[k]=True
                q.addq(k)
    
    return visited


def BFSList(Alist,v):
    vistited,parent={},{}
    for i in Alist.keys():
        vistited[i]=True
        parent[i]=None
        
    q=Queue
    
    while not q.isempty():
        j=q.deq()
        for k in Alist[j]:
            if not vistited[k]:
                vistited[k]=True
                parent[k]=j
    return (vistited,parent)
    
    