def QuickSort(L,l,u):
    if u-l <=1:
        return L
    pivot=L[l]
    upper=lower=l+1
    for i in range(l+1,u):
        if L[i] > pivot:
            upper+=1
        else:
            L[i],L[lower]=L[lower],L[i]
            upper+=1
            lower+=1
    L[l],L[lower-1]=L[lower-1],L[l]
    lower-=1
    print(L)
    QuickSort(L,l,lower)
    QuickSort(L,lower+1,u)
    return L
    
    
    
    
l=eval(input())
print(QuickSort(l,0,len(l)))