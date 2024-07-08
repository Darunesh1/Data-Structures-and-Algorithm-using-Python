import numpy as np

# Function to get the neighbors of a vertex
def neighbours(AMat, v):
    nbrs = []
    rows, cols = AMat.shape
    for i in range(rows):
        if AMat[v, i] == 1:
            nbrs.append(i)
    return nbrs

# Initialize visited and parent dictionaries
visited, parent = {}, {}

# Initialize DFS by setting up the visited and parent structures
def DFSInit(Amat):
    global visited, parent  # Use global to modify the variables defined outside this function
    rows, cols = Amat.shape
    
    for i in range(rows):
        visited[i] = False
        parent[i] = None

# Perform DFS on the graph
def DFS(Amat, v):
    # Mark the current node as visited
    visited[v] = True
    
    # Visit all the neighbors of the current node
    for i in neighbours(Amat, v):
        if not visited[i]:
            parent[i] = v
            DFS(Amat, i)
            
            
def DFSInitList(Alist):
    global visited, parent  # Use global to modify the variables defined outside this function
    for i in Alist.keys():
        visited[i] = False
        parent[i] = None
        
def DFSList(Alist,v):
    visited[v] = True
    
    for i in Alist[v]:
        if not visited[i]:
            parent[i] = v
            DFSList(Alist, i)