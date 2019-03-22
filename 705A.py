n = int(input())
a = "that I hate it"
b = "that I love it"
q = "I hate it"
for i in range(0,n):
    if(i==0):
        pass
    else:
        if(i%2==0):
            q = q.strip('it') + a
        elif(i%2 != 0):
            q = q.strip('it') + b
print(q)
