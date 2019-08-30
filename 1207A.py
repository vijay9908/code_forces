n = int(input())
for i in range(n):
    b , p , f = map(int,input().split())
    h , c = map(int,input().split())
    print(min(b//2,f)*c + max(0,min((b-(f*2))//2,p)*h));
    