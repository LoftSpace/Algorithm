import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

M , N = map(int,input().split())
dp = [[-1] * (N+1) for _ in range(M+1)]
grid = [[0]*(N+1) for _ in range(M+1)]

dRow = [1,-1,0,0]
dCol = [0,0,1,-1]

for i in range(1,M+1):
    temp = list(map(int,input().split()))
    for j in range(1,N+1):
        grid[i][j] = temp[j-1]


def dfs(row,col):
    if row == M  and col == N :
        return 1
    if dp[row][col] != -1 :
        return dp[row][col]
    
    ways = 0

    for dir in range(4) :
        nextRow = row + dRow[dir]
        nextCol = col + dCol[dir]
        if 1 <= nextRow <= M and 1 <= nextCol <= N :
            if grid[nextRow][nextCol] < grid[row][col] :
                ways += dfs(nextRow,nextCol)
    dp[row][col] = ways
    return ways
dfs(1,1)
print(dp[1][1])