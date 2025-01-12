from collections import deque
def solution(grid):
    M = len(grid)
    N = len(grid[0])
    answer = []
    dRow = [-1,0,1,0]
    dCol = [0,1,0,-1]
    visited = [[[False] * 4 for i in range(N)] for j in range(M)]
    def bfs(start_row,start_col,start_dir) :
        queue = deque()
        queue.append([start_row,start_col,start_dir,0])
       
        
        while queue :
            row,col,current_dir,count = queue.popleft()
            #print(row,col,current_dir,count)
            # 같은 지역 같은 방향 방문 체크
            if visited[row][col][current_dir] :
                # 사이클 확인
                if row == start_row and col == start_col and current_dir == start_dir and count!=0 :
                    
                    return count
                else :
                    continue
            else :
                visited[row][col][current_dir] = True
                
            
            
            nextRow , nextCol = row + dRow[current_dir], col + dCol[current_dir]
            
            #범위 밖일 시, 위치 조정
            if nextRow >= M :
                nextRow = 0
            elif nextRow < 0 :
                nextRow = M - 1
            elif nextCol >= N :
                nextCol = 0
            elif nextCol < 0 :
                nextCol = N - 1
           
            # 이동
            if grid[nextRow][nextCol] == 'S' :
                queue.append([nextRow,nextCol,current_dir,count + 1])
            elif grid[nextRow][nextCol] == 'R' :
                queue.append([nextRow,nextCol,(current_dir + 1)%4,count + 1])
            else :
                if current_dir == 0 :
                    queue.append([nextRow,nextCol,3,count + 1])
                else :
                    queue.append([nextRow,nextCol,current_dir - 1,count + 1])
        return 0
    
            
    for i in range(M) :
        for j in range(N) :
            for k in range(4):
                if not visited[i][j][k]:
                    length = bfs(i,j,k)
                    if length!=0 :
                        answer.append(length)
    answer.sort()
    return answer