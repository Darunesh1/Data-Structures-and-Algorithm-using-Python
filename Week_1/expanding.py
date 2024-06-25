def expanding(l):
    a=abs(l[0]-l[1])
    for i in range(1,len(l)-1):
        
        if a>=abs(l[i]-l[i+1]):
            return False
        a=abs(l[i]-l[i+1])
    return True



L = eval(input())
print(expanding(L))