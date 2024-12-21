import sys

input = sys.stdin.readline

n = int(input())

grid = []
dRow = [1,-1,0,0]
dCol = [0,0,1,-1]
dp = [[-1] * n for _ in range(n)]

for i in range(n):
    grid.append(list(map(int,input().split())))

def canMove(row,col):
   
    for dir in range(4):
        nextRow = row + dRow[dir]
        nextCol = col + dCol[dir]
        if nextRow < 0 or nextRow >= n or nextCol < 0 or nextCol >= n :
            return False
        
        if grid[nextRow][nextCol] > grid[row][col]:
            return True
    return False

def dfs(row,col):
   
    
    if dp[row][col] != - 1 :
        return dp[row][col]
    
    
    dp[row][col] = 1
       
    
    for dir in range(4):
        nextRow = row + dRow[dir]
        nextCol = col + dCol[dir]
        if 0<= nextRow < n and 0 <= nextCol < n :
            if grid[nextRow][nextCol] > grid[row][col] :
                dp[row][col] = max(dp[row][col], dfs(nextRow,nextCol) + 1) 
     
    return dp[row][col]
ans = []
for i in range(n):
    for j in range(n):
        ans.append(dfs(i,j))
print(max(ans))
