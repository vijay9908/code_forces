n = int(input())
a = list(map(int,input().split()))[:n]
b = []
count = 0
real_count = 0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if(a[i]==a[j]):
            count += 1
    if(count > 1):
        b.append(a[i])
    elif(count==1):
        real_count += 1
    count=0
q = []
for i in range(1,6):
    q.append(b.count(i))
w = []
for subset in q:
    if subset not in w:
        w.append(subset)
print(w)
print(real_count+len(w))

