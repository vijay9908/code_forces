q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    k = 0
    for i in range(n-1):
        if(abs(a[i+1]-a[i]) == 1):
            k = 1
            break
    if( k == 1):
        print(2)
    else:
        print(1)
    




