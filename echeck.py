n = list(map(str,input().strip()))
e_c = 0
for i in range(0,len(n)):
    if(n[i]=="e"):
        e_c += 1
if(e_c > 0):
    print("YES")
else:
    print("NO")