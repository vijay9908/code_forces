t = int(input())
for _ in range(t):
    y , z = map(int,input().split())
    if y==z:
        print('YES')
        for i in range(y):
            print(1,end=' ')
        print()
        continue
    if z>y:
        print('NO')
        continue
    if y%2==0:
        if z%2==0:
            print('YES')
            for i in range(z-1):
                print(1,end=' ')
            k = z-1
            print(y-k)
        else:
            if z*2>y:
                print('NO')
            else:
                print('YES')
                for i in range(z-1):
                    print(2,end=' ')
                k = (z-1)*2
                print(y-k)
    else:
        if z%2==0:
            print('NO')
        else:
            print('YES')
            for i in range(z-1):
                print(1,end=' ')
            print(y-(z-1))
        