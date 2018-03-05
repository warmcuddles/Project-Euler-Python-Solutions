import math
i=int(math.pow(2,1000))
def su(n):
    s=0
    while(n>0):
        rem=n%10
        n=n//10
        s+=rem
    print(s)
su(i)




    
    

