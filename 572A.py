na , nb = map(int,input().split())
k , m = map(int,input().split())
a = list(map(int,input().split()))[:na]
b = list(map(int,input().split()))[:nb]
if(a[k-1]<b[nb-m]):
    print("YES")
else:
    print("NO")