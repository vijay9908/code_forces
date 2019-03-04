n = int(input())
a = list(str(input()))
cour = 0
couu = 0
for i in range(0,len(a)):
    if(a[i]=="R"):
        cour += 1
    else:
        couu += 1
cour = cour**2
couu = couu**2
res = cour + couu
q = int(res**(0.5))
print(q)