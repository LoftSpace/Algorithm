import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

for i in range(1,N + 1):
    t, p = map(int,input().split())
    dp[i] = max(dp[i-1],dp[i])
    if i + t <= N + 1 :
        dp[i + t -1] = max(dp[i + t - 1] , dp[i - 1] + p)

print(dp[-1])