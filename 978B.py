n = int(input())
word = input()
count = 0 
sub = 0
for letter in word:
    if(letter == 'x'):
        count += 1
    else:
        count = 0
    if(count>2):
        sub += 1
print(sub)
    