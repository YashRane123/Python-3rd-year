# cook your dish here
t = int(input())
for i in range(t):
    n,k=map(int,input().split(" "))
    c=0
    for j in range(1,k+1):
        d = n%j
        c = max(d,c)
    print(c)
    