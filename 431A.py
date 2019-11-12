a = list(map(int,input().split()))[:4]
s = list(map(int,input().strip()))
sum = 0
for i in range(len(s)):
    sum += a[s[i]-1]
print(sum)