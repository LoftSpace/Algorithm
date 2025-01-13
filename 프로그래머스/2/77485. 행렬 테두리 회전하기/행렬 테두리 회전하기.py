def solution(rows, columns, queries):
    grid = [[0] * columns for _ in range(rows)]
    answer = []
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = i * columns + j + 1
    for query in queries :
        Min = 100000
        x1 , y1 = query[0] - 1, query[1] - 1
        x2 , y2 = query[2] - 1, query[3] - 1
        #  위 가로 이동
        temp = grid[x1][y2]
        for col in range(y2,y1,-1):
            Min = min(Min,grid[x1][col])
            grid[x1][col] = grid[x1][col - 1]
            
        # 오른쪽 아래 이동
        temp2 = grid[x2][y2] 
        for row in range(x2,x1,-1):
            Min = min(Min,grid[row][y2])
            grid[row][y2] = grid[row-1][y2]
        Min = min(Min,grid[x1 + 1][y2])
        grid[x1 + 1][y2] = temp
        
        # 아래 가로 이동 <-
        temp3 = grid[x2][y1]
        for col in range(y1,y2):
            Min = min(Min,grid[x2][col])
            grid[x2][col] = grid[x2][col + 1]
        Min = min(Min,grid[x2][y2 - 1])
        grid[x2][y2 - 1] = temp2
        
        # 왼쪽 위 이동
        for row in range(x1,x2):
            Min = min(Min,grid[row][y1])
            grid[row][y1] = grid[row + 1][y1]
        Min = min(Min,grid[x2 - 1][y1])
        grid[x2 - 1][y1] = temp3
        
        answer.append(Min)
  
    return answer