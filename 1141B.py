n = int(input())
a = list(map(int,input().split()))[:n]
b = a
for i in range(0,len(a)):
    b.append(a[i])
def maxio(arr, n): 
    count = 0 
    result = 0 
    n = len(b)
    for i in range(0, n):  
        if (b[i] == 0): 
            count = 0
        else:  
            count+= 1 
            result = max(result, count)       
    return result  

print(maxio(b,n))
