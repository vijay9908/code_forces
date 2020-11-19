n, k = map(int,input().split())
diff = 240 - k
i , p = 0 , 0
while p <= diff and i<=n:
    i += 1
    p += 5*i
print(i-1)