import sys
from collections import deque

input = sys.stdin.readline

N , L , R = map(int,input().split())
board = []

for i in range(N):
    board.append(list(map(int,input().split())))

ans = 0
visited = [[False] * N for _ in range(N)]
def init_visited():
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

while True :
    
    graph = [[] for _ in range(N * N)]
    start_point = []
    init_visited()
    # 그래프 연결
    for i in range(N):
        for j in range(N):
            isConnected = False
            if j + 1 < N : 
                if L <= abs(board[i][j] - board[i][j + 1]) <= R :
                    graph[i * N + j].append(i * N + j + 1)
                    graph[i * N + j + 1].append(i * N + j)
                    isConnected = True
                    
            if i + 1 < N : 
                if L <= abs(board[i][j] - board[i + 1][j]) <= R :
                    graph[(i + 1) * N + j].append(i * N + j)
                    graph[i * N + j].append((i + 1) * N + j)
                    isConnected = True
            if isConnected :
                start_point.append([i,j])

    if len(start_point) == 0 :
        print(ans)
        break

    queue = deque([])
    #각 시작점에서
    for s in start_point :
        # 연합 탐색
        if not visited[s[0]][s[1]] : 
            
            queue.append([s[0],s[1]])
            visited[s[0]][s[1]] = True
            people = 0
            path = []
            while queue :
                row,col = queue.popleft()
            
                people += board[row][col]
                path.append([row,col])
                for nextNode in graph[row * N + col] :
                    if not visited[nextNode // N][nextNode % N]:
                        visited[nextNode // N][nextNode % N] = True
                        queue.append([nextNode // N , nextNode % N])
        # 사람 분배
        devide_people = people // len(path)
        for node in path :
            board[node[0]][node[1]] = devide_people
    #for i in board :
     #   print(i)
    ans += 1
