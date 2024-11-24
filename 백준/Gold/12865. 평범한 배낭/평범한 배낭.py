import sys
input=sys.stdin.readline

num,total_weight = map(int,input().split())
weight=[0]
value=[0]
dp=[[0]*(total_weight+1) for _ in range(num+1)]
for i in range(num):
    w,v=map(int,input().split())
    weight.append(w)
    value.append(v)

for i in range(num+1):
    dp[i][0]=0

for i in range(total_weight):
    dp[0][i]=0

for i in range(1,num+1):
    for j in range(1,total_weight+1):
        if j < weight[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-weight[i]]+value[i],dp[i-1][j])
print(dp[num][total_weight])