# Problem 2: Gaussian elimination without and with partial
# pivoting.

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as npla
import scipy.linalg as spla



# Gaussian Elimination without partial pivoting for factorizing a
# linear system A x = b into A = L * U and b = L^{-1}x * b
#
# Inputs: Matrix A, Vector b
#
# Outputs: Solution x
#
def GE(A, b):

    # Your
    # function
    # definition
    # goes here\
    #n=len(b)
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


# Gaussian Elimination with partial pivoting for factorizing a
# linear system A x = b into P * A = L * U and b = L^{-1}x * P * b
#
# Inputs: Matrix A, Vector b
#
# Outputs: Solution x
#
# Note: The permutation matrix is not tracked
def GE_pp(A, b):
    
    # Your
    # function
    # definition
    # goes here
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

# pi=4
# ci=3
li=[10,20,30,40]
matchoice=[1,2,3]
for i in li:
    for j in matchoice:
        n=i
        matrix_choice=j
        print("\n************************n=",n,"***********************************")
        print("====================================================================")
        print("\n                   matrix_choice:",matrix_choice)
        print("====================================================================")
        # print("n=",n)
        A=[[0 for i in range(n)] for i in range(n)]
        # matrix_choice = 2   # 1, 2 or 3. Default: random

        if matrix_choice == 2:
            for i in range(0,n):
                for j in range(0,n):

                    A[i][j]=1/(i+j+1)

        elif matrix_choice == 3:
            for i in range(n):
                for j in range(n):
                    if(j<=i):
                        A[i][j]=1
                    else:
                        A[i][j]=-1
        else:
            np.random.seed(0)
            A = np.random.rand(n, n)



        x_star = np.ones(n)
        b = np.dot(A, x_star)
            
        # Computations as sought
        print ("\ncondition number: %g" % np.linalg.cond(A))
        print("\n====================================================================")
        # print()


        # Solve without pivoting
        x_npp = GE(A.copy(), b.copy())
        error_npp = np.linalg.norm(x_star - x_npp)
        residual_npp = np.linalg.norm(np.dot(A, x_npp) - b)
        print ("\n         TYPE         ","|\t Error      ","|\t Residual  ")
        print ("\nNo partial pivoting:  ","|\t",error_npp,"|\t",residual_npp)
        # print ("Error = %1.6g  Residual = %1.6g" %(error_npp, residual_npp))

        # Solve with partial pivoting
        x_pp = GE_pp(A.copy(), b.copy())
        error_pp = np.linalg.norm(x_star - x_pp)
        residual_pp = np.linalg.norm(np.dot(A, x_pp) - b)
        print ("\nWith partial pivoting:","|\t",error_pp,"|\t",residual_pp)
        # print ("\nwith partial pivoting:")
        # print ("Error = %1.6g  Residual = %1.6g" %(error_pp, residual_pp))
        # To be 
        # completed
        # by you

        # Solve using numpy.linalg's solve

        # To be 
        # completed
        # by you
        x_pps = np.linalg.solve(A.copy(), b.copy())
        error_pps = np.linalg.norm(x_star - x_pps)
        residual_pps = np.linalg.norm(np.dot(A, x_pps) - b)
        # print ("\nNo partial pivoting:","|\t",error_npp,"|\t",residual_npp)
        print ("\nwiht linalg solve  :  ","|\t",error_pps,"|\t",residual_pps)
        # print ("\nwith linalg solve:")
        # print ("Error = %1.6g  Residual = %1.6g" %(error_pps, residual_pps))








