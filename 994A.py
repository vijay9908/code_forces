n , m = map(int,input().split())
a = list(map(int,input().split()))[:n]
b = list(map(int,input().split()))[:m]
q = []
for i in range(0,n):
    for j in range(0,m):
        if(a[i]==b[j]):
            q.append(a[i])
for i in range(0,len(q)):
    print(q[i],end=" ")
            
        
