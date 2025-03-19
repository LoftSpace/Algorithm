import sys
from itertools import combinations
from collections import deque
import copy

n,m = map(int,input().split())
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
virus = []
def bfs():
    global answer
    count = 0
    queue = deque()
    temp = copy.deepcopy(graph)

    for v in virus :
        queue.append(v)
    while queue :
        x,y = queue.popleft()
        for dir in range(4):
            nextX = x + dx[dir]
            nextY = y + dy[dir]
            if 0 <= nextX < n and 0 <= nextY < m :
                if temp[nextX][nextY] == 0 :
                    temp[nextX][nextY] = 2
                    queue.append([nextX,nextY])
    
    for i in temp :
        for j in i :
            if j == 0 :
                count += 1
    
    answer = max(answer,count)
def makeWall(count):
    if count == 3 :
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 :
                graph[i][j] = 1
                makeWall(count + 1)
                graph[i][j] = 0

for i in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 :
            virus.append([i,j])
answer = 0
makeWall(0)
print(answer)