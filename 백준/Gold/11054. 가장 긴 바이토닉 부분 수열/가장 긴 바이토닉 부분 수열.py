import sys
input= sys.stdin.readline

n=int(input())

A=list(map(int,input().split()))

dp=[[1,0] for _ in range(n)]

for i in range(n):
    for j in range(i,-1,-1):
        if A[j] < A[i] :
            dp[i][0]= max(dp[i][0],dp[j][0]+1)

for i in range(n,-1,-1):
    for j in range(i,n):
        if A[j] < A[i] :
            dp[i][1]=max(dp[i][1],dp[j][1]+1)
max=0
for i in range(n):
    if max < dp[i][0]+dp[i][1]:
        max=dp[i][0]+dp[i][1]
print(max)
#print(dp)
