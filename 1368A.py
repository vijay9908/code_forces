t = int(input())
for _ in range(t):
    a , b , n = map(int,input().split())
    a , b = max(a,b) , min(a,b)
    count = 0
    while(b<=n):
        a,b = max(a,b) , a+b
        count += 1
    print(count)
        
    