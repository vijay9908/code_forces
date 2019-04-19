n, c = list(map(int, input().split()))

p = list(map(int, input().split()))
t = list(map(int, input().split()))

res1 = 0
t1 = 0
res2 = 0
t2 = 0
for i in range(n):
    t1 += t[i]
    res1 += max(p[i] - c * t1, 0)
    
    t2 += t[n - i - 1]
    res2 += max(p[n - i - 1] - c * t2, 0)

if res1 > res2:
    print('Limak')
elif res2 > res1:
    print('Radewoosh')
else:
    print('Tie')