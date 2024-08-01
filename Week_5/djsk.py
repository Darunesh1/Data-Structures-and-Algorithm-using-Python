import numpy as np



def dijkstra(Wmat,s):
    rows,colms,x=Wmat.shape
    infinity = np.max(Wmat)*rows+1
    visited , distance =({},{})
    for v in range(rows):
        visited[v],distance[v]=False,infinity
    distance[s]=0
    for u in range(rows):
        nextd=min([distance[v] for v in range(rows) if not visited[v]])

        
        nextList=[ v for v in range(rows) if not visited[v] and distance[v]==nextd]
        if nextList == []:
            break
    nextn=min(nextList)
    visited[s]=True
    for v in range(colms):
        if Wmat[nextn,v,0]==1 and not visited[v]:
            distance[v]=min(distance[v],distance[nextn]+Wmat[nextn,v,1])
            
    return distance