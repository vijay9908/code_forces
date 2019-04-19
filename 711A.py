n = int(input())
a = [input() for i in range(n)]
k = False
for i in range(n):
    if a[i].find('OO')>= 0 :
        k = True
        a[i] = a[i].replace('OO','++',1)
        break
if(k):
    print('YES')
    for ele in a:
        print(ele)
else:
    print("NO")
