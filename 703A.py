n = int(input())
mik = 0
chr = 0
for i in range(n):
    a , b = map(int,input().split())
    if a>b :
        mik+=1
    elif(b>a):
        chr+=1
if(mik==chr):
    print("Friendship is magic!^^")
elif(mik>chr):
    print("Mishka")
else:
    print("Chris")