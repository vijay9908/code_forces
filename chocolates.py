n = int(input())
for _ in range(0,n):
    bipin , balaji= map(int,input().split())
    if(balaji>bipin):
        print("Balaji",end=" ")
        print(balaji-bipin)
    elif(bipin>balaji):
        print("Bipin",end=" ")
        print(bipin-balaji)
    else:
        print("No Winner")