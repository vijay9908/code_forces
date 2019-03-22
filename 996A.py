n = int(input())
count = 0
deno = [100,20,10,5,1]
for i in range(0,len(deno)):
    count += n//deno[i]
    n %= deno[i]
print(count)