import sys

input = sys.stdin.readline

T = int(input())
for testcase in range(T) :
    N = int(input())
    table = []
    table.append(list(map(int,input().split())))
    table.append(list(map(int,input().split())))
   
    dp = [[0] * N for _ in range(3)]
    dp[0][0] = table[0][0]
    dp[1][0] = table[1][0]
    dp[2][0] = 0
    for col in range(1,N):
        for row in range(3):
            if row == 0 :
                dp[row][col] = max(dp[1][col-1],dp[2][col-1]) + table[row][col]
            elif row == 1 :
                dp[row][col] = max(dp[0][col-1],dp[2][col-1]) + table[row][col]
            else :
                dp[row][col] = max(dp[0][col-1],dp[1][col-1])
    Max = 0
    Max = max(dp[0][N-1],dp[1][N-1])
    Max = max(Max, dp[2][N-1])
    print(Max)