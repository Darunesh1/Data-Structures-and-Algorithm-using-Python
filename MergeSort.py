def MergeSort(l):
    n=len(l)
    if n<=1:
        return l
    
    L=MergeSort(l[:n//2])
    R=MergeSort(l[n//2:])
    
    B=Merge(L,R)
    
    return B




def Merge(L,R):
    n,m=len(L),len(R)
    c=[]
    i=j=k=0
    
    while k < m+n:
        if i==n:
            c.extend(R[j:])
            k=k+m-j
        elif j==m:
            c.extend(L[i:])
            k=k+n-i
        elif L[i]<R[j]:
            c.append(L[i])
            i+=1
            k+=1
        else:
            c.append(R[j])
            j+=1
            k+=1
    return c



l=eval(input())
print(MergeSort(l))