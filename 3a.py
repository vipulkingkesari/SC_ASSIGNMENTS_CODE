import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as npla
import scipy.linalg as spla
def GE_pp(A, b):
    
    # Your
    # function
    # definition
    # goes here
    n=len(A)
    l=[0 for i in range(n)]
    s=[0 for i in range(n)]
    for i in range(0,n):
        l[i]=i
        smax=0
        for j in range(0,n):
            smax=max(smax,abs(A[i][j]))
        s[i]=smax

    for k in range(0,n-1):
        rmax=0
        for i in range(k,n):
            r=A[l[i]][k]/s[l[i]]
            if r>rmax:
                rmax=r
                j=i

        ltemp=l[k]
        l[k]=l[j]
        l[j]=ltemp

        for i in range(k+1,n):
            amult=A[l[i]][k]/A[l[k]][k]
            A[l[i]][k]=amult
            for j in range(k+1,n):
                A[l[i]][j]=A[l[i]][j]-amult*A[l[k]][j]

    for k in range(0,n-1):
        for i in range(k+1,n):
            b[l[i]]=b[l[i]]-A[l[i]][k]*b[l[k]]


    x=[0 for i in range(n)]

    x[n-1]=b[l[n-1]]/A[l[n-1]][n-1]

    for i in range(n-2,-1,-1):
        sums=b[l[i]]
        for j in range(i+1,n):
            sums=sums-A[l[i]][j]*x[j]

        x[i]=sums/A[l[i]][i]










            
    return x



A=[[1,1,2*(10**9)],[2,-1,1000000000],[1,2,0]]
b=[1,1,1]
x_ans=GE_pp(A,b)
print(x_ans)
