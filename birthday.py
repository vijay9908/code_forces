n = int(input())
a = list(map(int,input().split()))
d,m = map(int,input().split())
count = 0

for i in range(0,len(a)):
    if(sum(a[i:i+m])==d):
        count += 1
print(count)

