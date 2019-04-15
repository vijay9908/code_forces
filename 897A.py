n , m = map(int,input().split())
a = list(input())
for i in range(m):
    l , r , c1 , c2 = map(str,input().split())
    for j in range(int(l),int(r)+1):
        if(a[j-1] == c1):
            a[j-1] = c2
print(''.join(a))