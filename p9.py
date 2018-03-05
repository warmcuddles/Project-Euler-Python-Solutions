#There exists exactly one Pythagorean triplet for which a + b + c = 1000,Find the product abc.
for m in range(1,1000,1):
    for n in range(1,1000,1):
        if(m<n):
            a = (n**2) - (m**2)
            b = 2*n*m
            c = (n**2) + (m**2)
            if(c<1000):
                if(a+b+c==1000):
                    print(a*b*c)
