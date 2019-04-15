n = int(input())
a = []
for i in range(n):
    b = input()
    if b not in a:
        print("NO")
        a.append(b)
    else:
        print("YES")