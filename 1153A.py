n , t = map(int,input().split())
count = 0
if(t<=n):
    count+=1
else:
    count = 0
for i in range(n):
    a, b = map(int,input().split())
    if b<= a:
        count+=1
print(count)