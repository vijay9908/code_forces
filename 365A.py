n , k = map(int,input().split())
k = list(range(k+1))
count = 0
for i in range(n):
    a = input()
    a = [int(r) for r in list(a)]
    for item in k:
        if item not in a:
            break
    else:
        count += 1
print(count)