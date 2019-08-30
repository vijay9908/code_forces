n = int(input())
for i in range(n):
    b , p , f = map(int,input().split())
    h , c = map(int,input().split())
    if(c > h):
        print(min(b//2,f)*c + max(0,min((b-(f*2))//2,p)*h));
    elif(b <= 1):
        print("0")
    else:
        print(min(b//2,p)*h + max(0,min((b-(p*2))//2,f)*c))