import sys

input = sys.stdin.readline
T = int(input())

for test in range(T):

    N = int(input())
    arr = list(map(int,input().split()))
    dp = [[1000000000] * (N+1) for _ in range(N+1)]

    sumArr = [0] * (N+1)

    for i in range(1,N + 1):
        sumArr[i] = sumArr[i-1] + arr[i-1]

    for i in range(1, N+ 1) :
        dp[i][i] = 0



    for n in range(1,N):
        for i in range(1, N-n + 1):
            j = i + n
            for k in range(i,j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + sumArr[j] - sumArr[i - 1])
                

    print(dp[1][N])