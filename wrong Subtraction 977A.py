n , k = map(int,input().split())
for i in range(0,k):
    if(n>0):
        if(n%10 != 0):
            n -= 1
        elif(n%10 == 0):
            n /= 10
print(int(n))

    