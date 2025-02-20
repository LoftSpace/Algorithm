def solution(board, skill):
    N = len(board)
    M = len(board[0])
    new_board = [[0] * (M + 1) for _ in range(N + 1)]
    answer = 0
    for s in skill :
        x1,y1,x2,y2 = s[1],s[2],s[3],s[4]
        degree = s[5]
        if s[0] == 1:
            degree = -degree
        new_board[x1][y1] += degree
        new_board[x2 + 1][y2 + 1] += degree
        new_board[x1][y2 + 1] += -degree
        new_board[x2 + 1][y1] += -degree
        
    
        
    for col in range(M + 1):
        for row in range(1, N + 1):
            new_board[row][col] += new_board[row-1][col]
    
    for row in range(N + 1):
        for col in range(1, M + 1):
            new_board[row][col] += new_board[row][col - 1]
     
    for i in range(N):
        for j in range(M):
            board[i][j] += new_board[i][j]
            if board[i][j] > 0 :
                answer += 1
    
    return answer