n = list(map(str,input().strip()))
m = []
for i in range(0,len(n)):
    if(n[i]=="e"):
        m.append(i)
if(len(m)==0):
    print("-1")
else:
    for i in range(0,len(m)):
        print(m[i]+1,end=" ")


        
        