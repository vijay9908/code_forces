n = int(input())
a = input()
i = 0
q = 0
while i < n-1:
    if a[i] == a[i+1]:
        i+=1
    else:
        i+=2
        q+=1
print (n-q)