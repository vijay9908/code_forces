from collections import Counter
n = int(input())
a = list(map(int,input().split()))[:n]
b = []
for i in range(0,len(a)):
    b.append(a.count(a[i]))
print(max(b))