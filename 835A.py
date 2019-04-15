n , v1 , v2 , t1 , t2 = map(int,input().split())
time1 = v1*n + t1*2
time2 = v2*n + t2*2
print("First" if time1<time2 else "Second" if time1>time2 else "Friendship")