n = input()
count = 0
if(len(set(n)) == 1):
    print("0")
elif(n == n[::-1]):
    print(len(n)-1)
else:
    print(len(n))
