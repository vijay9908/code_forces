a = []
for i in range(5):
    a.append(list(map(int,input().split()))[:5])
for i in range(5):
    for j in range(5):
        if(a[i][j] == 1):
            print(abs(i-3+1)+abs(j-3+1))
            break