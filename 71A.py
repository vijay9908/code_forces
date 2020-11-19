for _ in range(int(input())):
    s = input()
    k = len(s)
    if len(s)>10:
        print(s[0]+str((k-2))+s[-1])
    else:
        print(s)