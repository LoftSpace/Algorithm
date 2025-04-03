import sys

input = sys.stdin.readline

N , T = map(int,input().split())

dp = [[0] * (T + 1) for _ in range(N + 1)]
#print(dp)
w = [0] * (N + 1)
v = [0] * (N + 1)

for i in range(1,N + 1):
    a,b = map(int,input().split())
    w[i] = a
    v[i] = b

for i in range(1,N + 1):
    for j in range(1,T + 1):
        if j - w[i] >= 0 :
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]] + v[i])
        else :
            dp[i][j] = dp[i-1][j]
print(max(dp[N]))