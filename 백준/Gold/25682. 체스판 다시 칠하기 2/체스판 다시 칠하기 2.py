import sys

input = sys.stdin.readline

N , M , K = map(int,input().split())

grid = [input().strip() for _ in range(N)]

arrSum = [[0] * (M+1) for _ in range(N+1)]

for row in range(1,N+1) :
    for col in range(1,M+1) :
        if (row + col) % 2 == 0:
            if grid[row-1][col-1] == 'W' :
                arrSum[row][col] = arrSum[row][col-1] + arrSum[row-1][col] - arrSum[row-1][col-1] + 1
            else :
                arrSum[row][col] = arrSum[row][col-1] + arrSum[row-1][col] - arrSum[row-1][col-1]
        else :
            if grid[row-1][col-1] == 'B' :
                arrSum[row][col] = arrSum[row][col-1] + arrSum[row-1][col] - arrSum[row-1][col-1] + 1
            else :
                arrSum[row][col] = arrSum[row][col-1] + arrSum[row-1][col] - arrSum[row-1][col-1]
Min = 10000000000

for i in range(K,N+1) :
    for j in range(K,M+1) :
        case1 = arrSum[i][j] - arrSum[i-K][j] - arrSum[i][j-K] + arrSum[i-K][j-K]
        case2 = K*K - case1
        Min = min(Min,case1)
        Min = min(Min,case2)
print(Min)