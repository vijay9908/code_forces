t = int(input())
for _ in range(t):
    a , b = map(int,input().split())
    if(a>b):
        if(a%b==0):
            print("0")
        else:
            print(b-(a%b))
    else:
        print(b-a)