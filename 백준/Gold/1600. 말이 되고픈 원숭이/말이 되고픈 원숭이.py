import sys
from collections import deque
input = sys.stdin.readline
MAX = float('inf')
K = int(input())

W , H = map(int,input().split())
dRow = [1,-1,0,0]
dCol = [0,0,1,-1]
dRowHorse = [1,1,-1,-1,2,2,-2,-2]
dColHorse = [2,-2,2,-2,1,-1,1,-1]
queue = deque()
visited = [[[MAX] * (K+1) for _ in range(W)] for i in range(H)]
grid = []


for i in range(H):
    grid.append(list(map(int,input().split())))

#print(grid)
def bfs(startRow,startCol):
    queue.append([startRow,startCol,0,0])
    visited[0][0][0] = 0
    while queue :
        row, col, move, jump = queue.popleft()
        if row == H - 1 and col == W - 1 :
            print(move)
            return 
        for dir in range(4) :
            nextRow = row + dRow[dir]
            nextCol = col + dCol[dir]
            #범위 내
            if 0<= nextRow and nextRow < H and 0 <= nextCol and nextCol < W :
                # 이동 가능
                if grid[nextRow][nextCol] == 0 :
                    # 더 최단경로 
                    if visited[nextRow][nextCol][jump] > move + 1 :
                        visited[nextRow][nextCol][jump] = move + 1
                        queue.append([nextRow,nextCol,move + 1,jump])
            
        if jump < K :
            for dir in range(8):
                nextRow = row + dRowHorse[dir]
                nextCol = col + dColHorse[dir]
                
                 #범위 내
                if 0 <= nextRow and nextRow < H and 0 <= nextCol and nextCol < W :
                    #print(nextRow)
                    #print(nextCol)
                    if grid[nextRow][nextCol] == 0 :
                        if visited[nextRow][nextCol][jump + 1] > move + 1 :
                            visited[nextRow][nextCol][jump + 1] = move + 1
                            queue.append([nextRow,nextCol,move + 1, jump + 1])
    print(-1)
bfs(0,0)