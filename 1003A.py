from collections import Counter
p = int(input())
a = list(map(int,input().split()))[:p]
b = []
for i in range(0,len(a)):
    b.append(a.count(a[i]))
print(max(b))
