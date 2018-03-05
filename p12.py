import itertools,math
def tri():
    tn=0
    for i in itertools.count(1):
        tn+=i
        if fact(tn)>500:
            return tn

def fact(n):
    i=1
    c=0
    while i<=math.sqrt(n):
        if n%i==0:
            c+=1
            if i!=(n/i):
                c+=1
        i+=1
    return c

print(tri())
    





















































    
