# cook your dish here
t=int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split(" ")))
    l=len(li)
    sumo=0
    sume=0
    for x in range(l):
        if x%2==0:
            sume+=li[x]
        else:
            sumo+=li[x]
    print(max(sume,sumo))
        