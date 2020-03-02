a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
x=min(a,d)
awd=a-x
dwd=d-x
y=min(dwd,b,c)
z=min(d,b,c)
d2=d-z
g=min(d2,a)
first=x*e+y*f
second=z*f+g*e
print(max(first,second))
