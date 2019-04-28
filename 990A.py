t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n//2):
        if abs(ord(s[i]) - ord(s[n-i-1])) == 0 or abs(ord(s[i]) - ord(s[n-i-1])) == 2:
            cnt+=1
    if cnt == n//2:
        print('YES')
    else:
        print('NO')