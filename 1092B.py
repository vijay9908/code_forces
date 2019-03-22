n = int(input())
a = list(map(int,input().split()))[:n]
b = []
a.sort()
for i in range(0,n):
    if(i%2!=0):
        if(a[i]>a[i-1]):
            b.append( a[i] - a[i-1] )
        else:
            b.append( a[i-1] - a[i] )
print(sum(b))