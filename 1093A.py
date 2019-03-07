n = int(input())
for i in range(0,n):
    k = int(input())
    if(k<=7):
        print("1")
    else:
        print(int(k/7 +1))