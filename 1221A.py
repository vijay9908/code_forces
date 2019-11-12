n = int(input())
count  = 0
for _ in range(n):
    k = int(input())
    a = list(map(int,input().split()))
    b = []
    for ele in a:
        if(ele <= 2048):
            b.append(ele)
    if(sum(b)>=2048):
        print("YES")
    else:
        print("NO")
