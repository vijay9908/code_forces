a , b , c = map(int,input().split())
count = 0
while(a!=0):
    a -= 1
    b -= 1
    c -= 1
    count += 3
print(count+1)

