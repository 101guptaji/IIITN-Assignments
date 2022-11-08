n,r=map(int, input().split())
arr=list(map(int,input().split()))
cnt=0
dc={}
dp={}
for i in arr[::-1]:
    if (i*r in dp):
        cnt+=dp[i*r]
    if (i*r in dc):
        dp[i]=dp.get(i,0)+dc[i*r]
    dc[i] = dc.get(i, 0) + 1
print(cnt)

        
        