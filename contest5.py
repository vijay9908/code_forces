n = int(input())
while(n%10):
    if((n+1) %  10 == 0):
        n = n+1
        n = n/10
    else:
        n = n/10
print(n)