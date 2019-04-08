n = int(input())
a = list(map(int,input().split()))
print(a.count(1))
p = 1
for i in range(1 , n):
    if(a[i]!=1):
        p +=1
    else:
        print(p , end= ' ')
        p = 1
print(p)