n = int(input())
a = list(map(int,input().split()))[:n]
for i in range(0,n-1):
    if(i%2==0):
        a.remove(max(a))
    else:
        a.remove(min(a))
print(a[0])