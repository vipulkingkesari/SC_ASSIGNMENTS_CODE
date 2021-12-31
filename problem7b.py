# Problem 7b: Implementation of the Taylor series formula for
# estimation of the number e.
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy.linalg as npla
import scipy.linalg as spla


# Write some a looping construct to compute e by using the Taylor
# series sum. But, first, determine what stopping criterion you should
# use for determining if the sum has been computed.

i=1
e1=1
temp=1

while(temp!=0):
    temp=1/np.math.factorial(i)
    e1+=temp
    i+=1


error=abs(math.e-e1)

# Notice that you cannot, of course, compute infinitely many terms of
# the sum. Thus, you will need to truncate the sum. Where should
# truncate it. It cannot be some user specified number of
# terms. However, Problem 6(b) may given you some hint.


print("\nThe relative error in computing e via Taylor series " +"is %1.35f"%error)