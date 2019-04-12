n = int(input())
a = list(map(int,input().split()))[:n]
b = set(a)
b.discard(0)
print(len(b))