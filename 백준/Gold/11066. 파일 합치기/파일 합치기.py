import sys

input = sys.stdin.readline
T = int(input())

for test in range(T):

    N = int(input())
    arr = list(map(int,input().split()))
    arrSum = [0] * ( N + 1)
    for i in range(N):
        arrSum[i + 1] = arrSum[i] + arr[i]

    dp = [[1000000000] * (N + 1) for _ in range(N + 1)]
    for i in range(1,N + 1):
        dp[i][i] = 0
    for k in range(1,N):
        for i in range(1,N - k + 1):
            j = i + k
            for a in range(i,j):
                dp[i][j] = min(dp[i][j],dp[i][a] + dp[a + 1][j] + arrSum[j] - arrSum[i-1])
    
    
    print(dp[1][N ])