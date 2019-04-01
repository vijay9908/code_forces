n = int(input())
a = list(map(int,input().split()))
count = 0
b = []
for i in range(0,n-1):
    if(a[i+1]>=a[i]):
        count += 1
    elif(a[i+1]<a[i]):
        b.append(count)
        count = 0
    
print(len(b)+1)

        