def SelectionSort(l):
    n=len(l)
    if n<1:
        return l
    
    for i in range(n):
        m=i
        
        for j in range(i+1,n):
            if l[m]>l[j]:
                m=j
            
            
        l[i],l[m]=l[m],l[i]
    return l


l=eval(input())
print(SelectionSort(l))



# O(n^2)
        