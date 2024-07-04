def BinarySearch(n,l):
    if l==[]:
        return False
    
    m=len(l)//2
    
    if n==l[m]:
        return True
    
    if n<l[m]:
        return BinarySearch(n,l[:m])
    else:
        return BinarySearch(n,l[m+1:])
    
    
    
l=eval(input())
n=int(input())
print(BinarySearch(n,l))