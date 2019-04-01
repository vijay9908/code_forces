n=int(input())
l=list(map(int,input().split()))
l.sort()
if l[n-2]-l[0]<l[n-1]-l[1]:
    print(l[n-2]-l[0])
else:
    print(l[n-1]-l[1])