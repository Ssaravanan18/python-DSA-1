# sliding windows
arr=[-1,2,3,3,4,5,-2]
n=len(arr)
k=3
l=0
r=k
max_sum=0
while r<=n:
    sun=0
    for i in range(l,r):
        sun=sun+arr[i]

    if max_sum<sun:
        max_sum=sun

    l+=1
    r+=1
    
print(max_sum)
    
