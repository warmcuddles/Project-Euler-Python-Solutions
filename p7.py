#What is the 10001 prime number?
list=[]
low=2
while (len(list)<=10001):
    flag = 0
    for i in range(2,low//2,1):
        if(low%i==0):
            flag = 1
            break
    if (flag == 0):
        list.append(low)
    low+=1

print(list[-1])
