def prime_product(n):
    for i in range(2,n//2 + 1):
        if n % i == 0:
            a= n//i 
            if is_prime(i) and is_prime(a):
                return True
    return False

def is_prime(n):
    for i in range (2, n//2 +1):
        if n % i == 0:
            return False
    return True


n = int(input())
print(prime_product(n))

