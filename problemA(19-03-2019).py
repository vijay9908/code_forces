n , m = map(int,input().split())
k = n
count = 0
while(k<m):
    if(m%(2*k)==0 and n!=m):
        k *=2
        count = count + 1
    elif(m%(3*k)==0):
        k *=3
        count = count + 1
    elif(m<(2*n)):
        count = count - 1
        break
        
print(count)




    


