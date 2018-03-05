def c(n):
    li=[n]
    while(n!=1):
        
        if n%2==0:
            n=int(n/2)
        else:
            n=int(3*n+1)
        li.append(n)
    return li

le=0
for i in range(2,1000000):
    
    arr=c(i)
    a=len(arr)
    if le<a:
        le=a
        lar=i
        
print(lar)

##def c(n):
##    li=[n]
##    while(n!=1):
##        
##        if n%2==0:
##            n=int(n/2)
##        else:
##            n=int(3*n+1)
##        li.append(n)
##    print(len(li))
##for i in range(2,50):
##    c(i)



    
        

