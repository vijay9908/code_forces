from math import ceil

for _ in range(int(input())):
    a , b = map(int,input().split())
    a , b = max(a,b) , min(a,b)
    print(ceil((a-b)/10))