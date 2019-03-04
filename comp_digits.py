m,n = map(int,input().split())
j,k = map(int,input().split())
for i in range(0,j):
    a = m%10
    m //= 10
for l in range(0,k):
    b = n%10
    n //= 10
if(a==b):
    print("YES")
else:
    print("NO")