import numpy as dp
a=[
	[75],
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20, 4,82,47,65],
	[19, 1,23,75, 3,34],
	[88, 2,77,73, 7,63,67],
	[99,65, 4,28, 6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
	[ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23],
]

b=dp.array(a)



def f(arr,r,c):
    for i in range(r-1,-1,-1):
        for k in range(0,i+1):
            if arr[i+1][k]<arr[i+1][k+1]:
                arr[i][k]+=arr[i+1][k+1]
            else:
                arr[i][k]+=arr[i+1][k]
    return arr[0][0]
    
            
q=f(b,len(b)-1,len(b)-1)
print(q)
