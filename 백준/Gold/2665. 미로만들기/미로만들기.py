import sys
from collections import deque
input = sys.stdin.readline

dRow = [1,-1,0,0]
dCol = [0,0,1,-1]

N = int(input())
visited = [[-1]* N for _ in range(N)]
grid = []
for i in range(N):
    grid.append(list(input().strip()))

def BFS(startRow,startCol) :
    queue = []
    queue = deque()
    visited[0][0] = 0
    queue.append([startRow,startCol,0])

    while queue :
        row, col , count = queue.popleft()
        #print(row,col,count)

        for dir in range(4):
            nextRow = row + dRow[dir]
            nextCol = col + dCol[dir]
            #범위 내에 있다
            if 0<= nextRow < N and 0<= nextCol < N :
                #첫 방문이다
                if visited[nextRow][nextCol] == -1 :
                    #검정 방이다
                    if grid[nextRow][nextCol] == '0' :
                        queue.append([nextRow,nextCol,count + 1])
                        visited[nextRow][nextCol] = count + 1
                    #흰방이다
                    else :
                        queue.append([nextRow,nextCol,count])
                        visited[nextRow][nextCol] = count
                else :
                    #검정 방이다
                    if grid[nextRow][nextCol] == '0' :
                        #이 경로로 가는 것이 더 적게 부신다면
                        if count + 1 < visited[nextRow][nextCol] :
                            #print("%d %d -> %d %d 갱신"%(row,col,nextRow,nextCol))
                            visited[nextRow][nextCol] = count + 1
                            queue.append([nextRow,nextCol,count + 1])
                    #흰 방이다
                    else :
                        if count < visited[nextRow][nextCol] :
                            #print("%d %d -> %d %d 갱신"%(row,col,nextRow,nextCol))
                            visited[nextRow][nextCol] = count
                            queue.append([nextRow,nextCol,count])

BFS(0,0)
print(visited[N-1][N-1])