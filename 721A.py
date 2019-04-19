n = int(input())
a = list(map(str,input().split('W')))
b = []
for elements in a:
    if elements!='':
        b.append(len(elements))
print(len(b))
print(*b , end='')




    
