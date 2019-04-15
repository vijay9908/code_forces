n = int(input())
a = list(map(int,input().split()))[:n]
ch = 0
while(ch<n-1 and a[ch]<a[ch+1]):
    ch += 1
while(ch<n-1 and a[ch]==a[ch+1]):
    ch += 1
while(ch<n-1 and a[ch]>a[ch+1]):
    ch += 1
ch += 1
if(ch!=n):
    print("NO")
else:
    print("YES")