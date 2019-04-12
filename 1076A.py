n = int(input())
a = str(input())
a = list(a)
for i in range(n-1):
    if(a[i]>a[i+1]):
        a.remove(a[i])
        break
if(len(a)==n):
    a.remove(a[n-1])
print(''.join(a))
