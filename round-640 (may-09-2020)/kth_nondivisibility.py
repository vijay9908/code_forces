t = int(input())
for _ in range(t):
    n , k = map(int,input().split())
    q1 , q2 = k//(n-1),k%(n-1)
    subs = n*q1
    if q2==0:
        print(subs-1)
    else:
        print(subs+q2)

    
    
