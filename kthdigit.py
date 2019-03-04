n = int(input())
k = int(input())
for i in range(0,k):
    b = n%10
    n //= 10
print(b)