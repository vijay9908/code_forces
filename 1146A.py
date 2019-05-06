a = input()
count1 = 0
count2 = 0
for i in range(len(a)):
    if(a[i] == 'a'):
        count1 += 1
count2 = len(a)-count1
if(count1>count2):
    print(len(a))
else:
    print(2*count1 - 1)

