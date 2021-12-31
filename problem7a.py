# Problem 7a: Implementation of the formula (n + 1/n)**n for
# estimation of the number e.
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy.linalg as npla
import scipy.linalg as spla

def e_by_limit(n):
    # Here n is the value

    # Your code for computing
    # e_n using the formula
    # goes here
    e_n=(1+(1/n))**n

    
    return e_n


# Write some initializing statements and
# a looping construct within which to call
# the above function. Accumlate the error
# for each n in err_n

result=[]
for i in range(1,16):
    temp=10**i
    t=math.e-e_by_limit(temp)
    result.append(t)




# Plot err_n versus n.
# Note that a log scale for the x-axis is better suited in displaying
# this plot.
N = [10**k for k in range(1, 16)]
plt.figure()
plt.semilogx(N, result, 'bo')
plt.grid(True)
plt.ylabel("$|e - (1 + 1/n)^n|$")
plt.xlabel("$n$")
plt.title("Error in computing e using the limit formula", fontsize=14)
plt.savefig("problem7a.pdf")
plt.show()


# Remark: The error plot here is an example where you should not be
# plotting a continuous curve since the error is for different values
# of natural numbers n 