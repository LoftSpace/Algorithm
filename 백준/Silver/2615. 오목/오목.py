import sys
from collections import deque

input = sys.stdin.readline

board = [list(map(int,input().split())) for _ in range(19)]

def isWin(row,col,dir,color):
    count = 0
    i = 0
    if dir == 'right' :
        if col - 1 >= 0 : # 이전 자리가 있다면
            #출발점이 맞다면
            if board[row][col - 1] == color :
                return False
        while  col + i < 19 and board[row][col + i] == color:
            i += 1
            count += 1
    elif dir == 'down' :
        if row - 1  >= 0 :
            if board[row-1][col] == color :
                return False
        while row + i< 19 and board[row + i][col] == color :
            i += 1
            count += 1
    elif dir == 'rightUp' :
        if col - 1 >= 0 and row + 1 < 19 :
            if board[row+1][col-1] == color :
                return False
        while row - i >= 0 and col + i < 19 and board[row - i][col + i] == color :
            i += 1
            count += 1
    elif dir == 'rightDown':
        if col - 1 >= 0 and row - 1 >= 0 :
            if board[row-1][col-1] == color :
                return False
        while row + i < 19 and col + i < 19 and board[row+i][col + i] == color :
            i += 1
            count += 1

    if count ==5 :
        return True
    else :
        return False
    
for i in range(19):
    for j in range(19):
        if board[i][j] != 0 :
            if  isWin(i,j,'right',board[i][j])  or isWin(i,j,'down',board[i][j]) or isWin(i,j,'rightUp',board[i][j]) or  isWin(i,j,'rightDown',board[i][j]) :
                print(board[i][j])
                print("%d %d"%(i+1,j+1))
                exit(0)
print(0)