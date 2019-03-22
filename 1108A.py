k = int(input())
a = []
for i in range(0,k):
    a = list(map(int,input().split()))
    if(a[1]!=a[3]):
        print(a[1],a[3])
    else:
        print(a[0],a[1])