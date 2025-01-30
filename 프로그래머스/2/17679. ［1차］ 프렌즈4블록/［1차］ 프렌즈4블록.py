def solution(m, n, boards):
    board = []
    answer = 0
    
    for i in boards :
        board.append(list(i))
    
    def update_board():
        for col in range(n):
            temp = []
            for row in range(m-1,-1,-1):
                if board[row][col] != '0' :
                    temp.append(board[row][col])
            for i in range(m - len(temp)):
                temp.append('0')
           
            for row in range(m):
                board[row][col] = temp[-row-1]
                
    def delete(delete_position):
        count = 0
        for position in delete_position:
            row = position // n
            col = position % n
            board[row][col] = '0'
            count += 1
       
        return count
    def check():
        
        delete_position = set()
        for start_row in range(m - 1):
            for start_col in range(n - 1):
                if board[start_row][start_col] != '0' and board[start_row][start_col] == board[start_row][start_col + 1] and board[start_row][start_col] == board[start_row + 1][start_col] and board[start_row][start_col] == board[start_row + 1][start_col + 1] :
                    delete_position.add(start_row * n + start_col)
                    delete_position.add((start_row + 1) * n + start_col)
                    delete_position.add((start_row) * n + start_col + 1)
                    delete_position.add((start_row + 1) * n + start_col + 1)
        
        return delete(delete_position)

    
  
    
    while  True :
        a = check()    
        if a == 0 :
            break
        else :
            answer += a
            update_board()
        
    return answer