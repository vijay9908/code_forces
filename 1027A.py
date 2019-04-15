k = int(input())
for _ in range(k):
    n = int(input())
    a = input()
    for i in range(n//2): 
        z = abs(ord(a[i])-ord(a[n-i-1]))
    if(z!=0 and z!=2):
        print("NO")
    else:
        print("YES")
