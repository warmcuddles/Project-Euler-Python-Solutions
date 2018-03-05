#The largest palindrome of product of two 3-digit numbers
list=[]
for x1 in range(100,1000, 1):
    for x2 in range(1000,100, -1):
        if (x1 != x2):
            n = x1 * x2
            temp = n
            rev = 0
            while (n > 0):
                dig = n % 10
                rev = rev * 10 + dig
                n = n // 10
            if (temp == rev):
                list.append(temp)
                list.sort()
element = 0
for x in list:
    element+=1
print(element)
print(list)
print("The largest palindrome is",list[-1])
















