
def d(n):
    li=[]
    for i in range(1,n//2+1):
        if(n % i==0):
            li.append(i)
    return sum(li)

qw=[]
for i in range(1,10000):
      a=d(i)
      b=d(a)
      if(b==i and a!=i):
          qw.append(a)
          qw.append(i)
print(sum(set(qw)))
          
























