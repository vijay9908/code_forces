n , h = map(int,input().split())
cou = 0
a = list(map(int,input().split()))[:n]
for i in a:
    if i > h:
        cou += 2
    else:
        cou += 1
print(cou)