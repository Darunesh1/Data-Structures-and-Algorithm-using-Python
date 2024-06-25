def histogram(l):
    li=[]
    a=[]
    for i in range(len(l)):
        if l[i] in a:
            continue
        li.append((l[i],l.count(l[i])))
        a.append(l[i])
        
    
    return sorted(sorted(li,key=fun),key=func)
    
    

def func(c):
    return c[1]
    
def fun(c):
    return c[0]



L=eval(input())
print(histogram(L))