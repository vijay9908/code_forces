n = int(input())
for _ in range(n):
    size = int(input())
    a = input().split('A')
    if(len(a)==1):
        print(0)
        continue
    else:
        a = a[1:]
    print(len(max(a)))




