import sys
from collections import deque

input = sys.stdin.readline
c=0

# 해당 경우의 수의 원소들이 모두 인접한지 확인
## S를 제외한 모든 위치를 visited[] = 1로 두고 0인 곳을 방문 하며 check + 1. check 가 7이면 
## 경로에있는 모든 위치를 방문했다는 뜻
def bfs(route):
    dRow = [1,-1,0,0]
    dCol = [0,0,1,-1]
    visited = [[1] * 5 for _ in range(5)]
    for i in route:
        visited[i[0]][i[1]] = 0
    queue = deque([(route[0])])
    

    visited[route[0][0]][route[0][1]] = 1

    check = 1
    while queue :
        row , col = queue.popleft()
        # 각 방향에 대해 
        for dir in range(4):
            nextRow = row + dRow[dir]
            nextCol = col + dCol[dir]
            # 범위 내
            if 0 <= nextRow < 5 and 0 <= nextCol < 5 :
                # 인접하면 이동
                if visited[nextRow][nextCol] == 0 :
                    visited[nextRow][nextCol] = 1
                    check += 1
                    queue.append((nextRow,nextCol))
    
    if check == 7 :
        return True
    else :
        return False

def dfs(move,start,yCount):
    global ans
    global c
    
    if yCount >= 4:
        return
    if move == 7 :
        #인접한지 확인
        if bfs(route):
            
            ans += 1
        return 
    #다음 위치
    for i in range(start , 25):
        row = i // 5
        col = i % 5
        if grid[row][col] == 'Y' :
            
            c += 1
        
        route.append((row,col))
        dfs(move + 1, i + 1, yCount + (grid[row][col] == 'Y'))
        route.pop()
ans = 0

route = []


grid = [list(input()) for _ in range(5)]

dfs(0,0,0)
print(ans)