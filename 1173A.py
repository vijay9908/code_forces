if __name__ == "__main__":
    pass
n = int(input())
for i in range(n):
    s = int(input())
    a = input()
    count = 0
    for j in range(len(a)):
        if(a[j]=="8"):
            count+=1
    if(count>0):
        print("YES")
    else:
        print("NO")



