import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
dp = [0]* n
dp[0] = 1
for i in range(0,n):
    dp[i] = 1
    for k in range(0,i):
        if arr[k] > arr[i]:
            dp[i] = max(dp[i],dp[k] + 1)

print(max(dp))