import sys

input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

dp = [[0] * 2 for _ in range(N)]
if N == 1 :
    print(arr[0])
    exit(0)
dp[0][0] = 0
dp[0][1] = arr[0]
dp[1][1] = arr[0] + arr[1]
dp[1][0] = arr[0]

for i in range(2,N):
    dp[i][0] = max(dp[i-1][1],dp[i-1][0])
    dp[i][1] = max(dp[i-2][0] + arr[i-1] + arr[i],dp[i-2][1] + arr[i])
print(max(dp[N-1]))