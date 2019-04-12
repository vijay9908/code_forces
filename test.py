n = int(input())
cou = 0
while(n%2==0):
    if(n%2==0):
        cou += 1
        n /= 2
print(cou)