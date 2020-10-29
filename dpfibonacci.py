def dpfib(n):
    fibarr=[0, 1]
    while len(fibarr)< n+1:
        fibarr.append(0)
    if n<=1:
        return n
    else:
        if fibarr[n-1]==0:
            fibarr[n-1]= dpfib(n-1)
        if fibarr[n-2]==0:
            fibarr[n-2]= dpfib(n-2)
    fibarr[n]= fibarr[n-2] + fibarr[n-1]
    return fibarr[n]

n=int(input("Enter range of the sequence: "))
for i in range(n):
    print(dpfib(i), end=" ")
