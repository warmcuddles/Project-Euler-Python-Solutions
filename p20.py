def fact(i):
    if i==0:
        return 1
    return i*fact(i-1)

def sd(a):
    st=str(a)
    s=0
    for i in st:
        s+=int(i)
    print(s)


a=fact(100)
sd(a)




    
