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





def dijkstralist(WList,s):
    infinity= 1+ len(WList.keys())* max([d for u in WList.keys() for (v,d) in WList[u]])
    vistited , distance ={},{}
    for v in WList.keys():
        vistited[v],distance[v]=True,infinity
    distance[s]=0
    for u in WList.keys():
        nextd=min([distance[v] for v in WList.keys() if not vistited[v]])
        
        nextList=[v for v in WList.keys() if not vistited[v] and distance[v]==nextd]
        
        if nextList == []:
            break
        
    nextn=min(nextList)
    vistited[s]=True
    for (v,d) in WList[nextn]:
        if not vistited[v]:
            distance[v]=min(distance[d],distance[nextn])
            
    return distance