def Insert(l,v):
    n=len(l)
    print(l,v)
    if n==0:
        return ([v])
    if v >= l[-1]:
        return (l+[v])
    else:
        return (Insert(l[:-1],v)+[l[-1]])
    
    
    
def Isort(l):
    n=len(l)
    if n<1:
        return l
    print(l)
    L=Insert(Isort(l[:-1]),l[-1])
    return L



l=eval(input())
print(Isort(l))