n,r=map(int,input().split())
for i in range(1,r+1):
    if n*i>=r:
        break
    print(n,"X",i,"=",n*i)
