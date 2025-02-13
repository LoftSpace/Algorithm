from collections import deque
def solution(board):
    def get_dir(row,col,nextRow,nextCol):
        #좌우 이동
        if row == nextRow :
            if nextCol == col + 1:
                return 0
            else :
                return 2
        # 상하이동
        else :
            if nextRow == row + 1 :
                return 1
            else : 
                return 3
                    
        
    INF = 1e8
    N = len(board)
    visited = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    dRow = [1,-1,0,0]
    dCol = [0,0,1,-1]
    queue = deque([])
    if board[0][1] != 1 :
        visited[0][1][0] = 100
        queue.append([0,1,100,0])
    if board[1][0] != 1 :
        visited[1][0][1] = 100
        queue.append([1,0,100,1])
    
    while queue :
        row,col,cost,cur_dir = queue.popleft()
        if row == N - 1 and col == N - 1 :
            continue
        
        for dir in range(4):
            nextRow = row + dRow[dir]
            nextCol = col + dCol[dir]
            #이동가능
            if 0 <= nextRow < N and 0 <= nextCol < N and board[nextRow][nextCol] != 1:
                next_dir = get_dir(row,col,nextRow,nextCol)
                # 방향변경
                if cur_dir != next_dir:
                    new_cost = cost + 100 + 500
                #방향 변경 안함
                else :
                    new_cost = cost + 100
                # 비용 갱신 가능
                if visited[nextRow][nextCol][next_dir] > new_cost: 
                    visited[nextRow][nextCol][next_dir] = new_cost
                    queue.append([nextRow,nextCol,new_cost,next_dir])
    
    
    answer = min(visited[N-1][N-1])
    return answer