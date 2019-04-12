n = int(input())
a = list(map(int,input().split()))[:n]
ch1 = 0
ch2 = 0
ch3 = 0
for i in range(1,n):
    if(a[i-1]<a[i] or a[i-1]==a[i]):
        ch1 = 1
    if(a[i-1]==a[i]):
        ch2 = 2
    if(a[i-1]>a[i]):
        ch3 = 3
    if(a[n-2]<a[n-1] or a[n-2]==a[n-1]):
        ch3 = 1
if(ch1==1 and (ch2==2 or ch2==0) and ch3==3):
    print("YES")
else:
    print("NO")