count = 0
n , k = map(int,input().split())
for _ in range(n):
    a = list(map(int,input().split()))
    if a.count(1) >=2:
        count += 1
print(count)