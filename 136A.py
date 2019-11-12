from sys import stdin
n = int(input())
a = list(map(int,input().split()))[:n]
for i in range(n):
    print(a.index(i+1)+1)
