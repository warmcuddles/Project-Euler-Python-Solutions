'''To solve this problem first check the answer for 1X1 matrix
,2X2 matrix,3X3 matrix answers: 2,6,20 resp now as we have to
reach from top to bottom lets start from 1st point which is
top-left corner of 1st box[0][0] from this point we have 2
points where we can move next, choose to move to any point and
again we will have 2 more points to move to and this will keep
on going until we reach Nth point
So, it involves making exactly N moves right and N moves down
in some order and we should not repeat the pattern so, at every
point one can pick one of the 2 points and hence there are
exactly  N things selected from 2N things which is C(2*(N),N)
'''

from math import factorial as fact
def combination(n, r):
	#0<=r<=n
	return fact(n)//(fact(r) * fact(n - r))
a=combination(2*20,20)
print(a)


    
