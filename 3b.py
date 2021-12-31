def GE(A, b):

    # Your
    # function
    # definition
    # goes here\
    n=len(b)
    for i in range(0,n):      
      temp = max(A[i])          
      b[i]=b[i]/temp            
      for j in range(n):
        A[i][j] = A[i][j]/temp
    for k in range(0,n-1):
        for i in range(k+1,n):
            temp=A[i][k]/A[k][k]
            A[i][k]=temp
            for j in range(k+1,n):
                A[i][j]=A[i][j]-temp*A[k][j]

            b[i]=b[i]-temp*b[k]

    x=[0 for i in range(n)]
    

    x[n-1]=b[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):  #n-2
        sums=b[i]
        for j in range(i+1,n):
            sums=sums-A[i][j]*x[j]
        x[i]=sums/A[i][i]




    
    return x

A=[[1,1,2*(10**9)],[2,-1,1000000000],[1,2,0]]
b=[1,1,1]
x_ans=GE(A,b)
print(x_ans)
