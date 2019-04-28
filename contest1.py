n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []
k = 1000000
for i in range(n):
    c.append((a[i]+b[i])%n)

def minimizeWithKSwaps(c, n, k): 
  
    for i in range(n-1): 
  
         
        pos = i 
        for j in range(i+1, n): 
  
    
            if (j-i > k): 
                break
  
            
            if (c[j] < c[pos]): 
                pos = j 
  
        
        for j in range(pos, i, -1): 
            c[j],c[j-1] = c[j-1], c[j] 
  
        
        k -= pos - i 
for i in range(n):
    print(c[i] , end='')