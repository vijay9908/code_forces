t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    k = 0
    while n>0:
        a.append((n%10)*10**k)
        n = n//10
        k += 1
    while 0 in a: a.remove(0)
    print(len(a))
    print(*a)
