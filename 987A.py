n = int(input())
d = {'purple':'Power','green':'Time','blue':'Space','orange':'Soul','red':'Reality','yellow':'Mind'}
for i in range(0,n):
    a = str(input())
    d.pop(a)
print(len(d))
for color,power in d.items():
    print(power)