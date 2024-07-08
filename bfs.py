import numpy as np
from queue_module import Queue

def neighbours(AMat, v):
    nbrs = []
    rows, cols = AMat.shape
    for i in range(rows):
        if AMat[v, i] == 1:
            nbrs.append(i)
    return nbrs

def BFS(AMat, v):
    rows, cols = AMat.shape
    visited = {}
    for i in range(rows):
        visited[i] = False 
    q = Queue()  # Instantiate the Queue

    visited[v] = True
    q.addq(v)
    
    while not q.isempty():
        j = q.deq()
        for k in neighbours(AMat, j):
            if not visited[k]:
                visited[k] = True
                q.addq(k)
    
    return visited

def BFSList(Alist, v):
    visited, parent = {}, {}
    for i in Alist.keys():
        visited[i] = False
        parent[i] = None
        
    q = Queue()  # Instantiate the Queue
    visited[v] = True
    q.addq(v)
    
    while not q.isempty():
        j = q.deq()
        for k in Alist[j]:
            if not visited[k]:
                visited[k] = True
                parent[k] = j
                q.addq(k)
                
    return (visited, parent)

def BFSLevel(Alist, v):
    level, parent = {}, {}
    for i in Alist.keys():
        level[i] = -1
        parent[i] = None
        
    q = Queue()  
    q.addq(v)
    level[v] = 0
    
    while not q.isempty():
        j = q.deq()
        for k in Alist[j]:
            if level[k] == -1:
                level[k] = level[j] + 1
                parent[k] = j
                q.addq(k)
                
    return (level, parent)
