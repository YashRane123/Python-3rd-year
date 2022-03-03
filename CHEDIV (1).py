
t=int(input())
for i in range(t):
    n,x,y=map(int,input().split(" "))
    li=list(map(int,input().split(" ")))
    res=0
    for j in li:
        if j%y==0 and j<=x:
            res+=1
    print(res)