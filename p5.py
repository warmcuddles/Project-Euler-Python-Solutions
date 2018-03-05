'''smallest positive number that is divisible by all of the
numbers from 1 to 20'''
i=0
s=0
while(s<14):
    i+=20
    s=0
    for x in range(2,21,1):
        if((x==2)or(x==5)or(x==10)or(x==20)or(x==4)):
            continue
        if(i%x==0):
            s+=1;
    if(s==14):
        print(i)
        break

