a = str(input())
n = len(a)
count = 0
for i in range(len(a)//2):
    if(a[i] != a[n-i-1]):
        count += 1
if(count==1 or (count==0 and len(a)%2!=0)):
    print("YES")
else:
    print("NO")
