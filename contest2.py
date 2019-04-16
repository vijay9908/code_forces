n = int(input())
a = list(map(int,input().split()))
uniques = sorted(set(a)) 
if len(uniques) == 1: 
    print("0") 
elif len(uniques) == 2: 
    print((uniques[1] - uniques[0])) 
elif(len(uniques)== 3):
    if((uniques[1]-uniques[0])==(uniques[2]-uniques[1])):
        print(uniques[1]-uniques[0])
    else:
        print("-1")