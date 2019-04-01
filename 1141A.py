n,m=map(int,input().split())
k=0
f=m//n
if m%n!=0:
    print(-1)
else:
    while f%2 == 0:
        f=f//2
        k+=1
    while f%3==0:
        f=f//3
        k+=1
    if f==1:
        print(k)
    else:
        print(-1)
