n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
k = int(input())
count = 0
for i in range(n):
    if(a[i][1] >= k):
        count += 1
print(count)