import math
low=int(input("enter the lower bound to prime no."))
high=int(input("enter the upper bound to prime no."))
li=[]
while(low<high):
    flag=0
    if low==1:
        flag=1
    for i in range(2,int(math.sqrt(low))+1):
        if(low % i == 0):
            flag = 1
            break
    if(flag == 0):
        li.append(low)
    low+=1
print(sum(li))

    
##import math
##
##
##def check_prime(num):
##    if num > 2 and num % 2 == 0:
##        return False
##    else:
##        # I tried using a generator here,
##        # but it is slower by a noticeable amount.
##        for i in range(3, int(math.sqrt(num)) + 1, 2):
##            if num % i == 0:
##                return False
##    return True
##
##
##def find_sum(limit):
##    sum = 0
##    for i in range(2, limit):
##        if check_prime(i):
##            sum += i
##    
##    return sum
##
##
##if __name__ == '__main__':
##
##    # Find the sum of all primes below two million
##    print(find_sum(2000000))
