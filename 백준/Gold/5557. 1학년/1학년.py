import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))

dp = [[0] * 21 for _ in range(N)]

dp[1][arr[0]] = 1

for i in range(2,N):
    for j in range(0,21):
        if j-arr[i-1] >= 0 : # 이전 수에 더해서 만드는 경우
            dp[i][j] += dp[i-1][j - arr[i-1]]  
        if j + arr[i-1] <= 20: #이전 수에 빼서 만드는 경우
            dp[i][j] += dp[i-1][j + arr[i-1]]
print(dp[N-1][arr[-1]])