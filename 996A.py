q = int(input())
count = 0
deno = [100,20,10,5,1]
for i in range(0,len(deno)):
    count += q//deno[i]
    q %= deno[i]
print(count)
