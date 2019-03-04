n = int(input())
sum = 0
a = list(map(int,input().split()))[:n]
for i in range(0,len(a)):
    sum += a[i]
print(sum)