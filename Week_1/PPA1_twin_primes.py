def Twin_Primes(n,m):
    l=[]
    for i in range(n,m+1):
        if isprime(i):
            if isprime(i+2) and i+2 <=m:
                l.append((i,i+2))
    return l 



def isprime(n):
    if n<2:
        return False
        
    for i in range (2, n//2 +1):
        if n % i == 0:
            return False
    return True    



n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))