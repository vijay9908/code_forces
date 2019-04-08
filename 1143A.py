n = int(input())
a = list(map(int,input().split()))[:n]
count1 = 0
count0 = 0
for i in range(n):
    if(a[i]==1):
        count1 = i+1
    elif(a[i]==0):
        count0 = i+1
print(min(count1 , count0))
    
    