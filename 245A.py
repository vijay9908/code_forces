n = int(input())
result1 = 0
result2 = 0
for i in range(n):
    ttt, pos, neg = list(map(int, input().split()))

    if ttt == 1:
        result1 += pos-neg
    else:
        result2 += pos-neg

print('LIVE' if result1 >= 0 else 'DEAD')
print('LIVE' if result2 >= 0 else 'DEAD')

