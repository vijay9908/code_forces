a = list(input().strip())
b = input()
k = 0 
c = 0
for i  in range(0,len(b)):
    if(a[k]==b[i] or a[k+1]==b[i]):
        c = 1
if(c==1):
    print("YES")
else:
    print("NO")



