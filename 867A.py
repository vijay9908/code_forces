n = int(input())
m = str(input())
a = list(m)
stof = 0
ftos = 0
for i in range(0,len(a)-1):
    if(a[i] == "F" and a[i+1]=="S"):
        ftos +=1
    elif(a[i] == "S" and a[i+1]=="F"):
        stof +=1
if(stof>ftos):
    print("YES")
else:
    print("NO")