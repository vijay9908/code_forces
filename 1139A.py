n = int(input())
a = str(input())
count = 0
for i in range(0,len(a)):
    if(int(a[i])%2==0):
        count += (i+1)
print(count)