s = input()
res = ''
mx = s[0]
for i in range(len(s)):
    mx = max(mx, s[i])
for i in range(len(s)):
    if s[i] == mx:
        res += s[i]
print(res)