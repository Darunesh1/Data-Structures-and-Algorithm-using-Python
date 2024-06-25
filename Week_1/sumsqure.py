def sumsquare(l):
    sumeven=sumodd=0
    for i in range(len(l)):
        if l[i] % 2==0:
            sumeven+=l[i] * l[i]
        else:
            sumodd+=l[i]*l[i]
    return [sumodd,sumeven]



L = eval(input())
print(sumsquare(L))