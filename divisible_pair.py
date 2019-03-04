n , k = map(int,input().split())
a = list(map(int,input().split()))[:n]
count = 0
b = []
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if((a[i]+a[j])%k==0 and i<j):
            b.append([a[i],a[j]])
#q = []
#for sub_list in b:
    #if sub_list not in q:
     #   q.append(sub_list)
#print(len(q))
print(len(b))
