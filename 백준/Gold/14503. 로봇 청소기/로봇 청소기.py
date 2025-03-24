import sys


input = sys.stdin.readline
N , M = map(int,input().split())
startRow, startCol, cur_dir = map(int,input().split())
dRow = [-1,0,1,0]
dCol = [0,1,0,-1]
board = [] 

def isAllClean(row,col):
    for dir in range(4):
        nextRow = row + dRow[dir]
        nextCol = col + dCol[dir]
        if 0 <= nextRow < N and 0 <= nextCol < M :
            if board[nextRow][nextCol] == 0 :
                return False
    return True

def move_backward(row,col,dir):
    backward_dir = (dir + 2) % 4
    nextRow = row + dRow[backward_dir]
    nextCol = col + dCol[backward_dir]
    if 0 <= nextRow < N and 0 <= nextCol < M :
        #작동 중지
        if board[nextRow][nextCol] == 1 :
            return -1,-1
        #후진
        else :
            return nextRow,nextCol
        
def rotate(row,col,count):
    global cur_dir
    if count == 4 :
        return row,col
    cur_dir = (cur_dir - 1) % 4
    nextRow = row + dRow[cur_dir]
    nextCol = col + dCol[cur_dir]
    #전진 가능 : 전진
    if 0 <= nextRow < N and 0 <= nextCol < M :
        if board[nextRow][nextCol] == 0 :
            return nextRow,nextCol
    #전진 불가 : 회전
    return rotate(row,col,count + 1)

for i in range(N):
    board.append(list(map(int,input().split())))


row = startRow
col = startCol
move = 0

while True :
   # print(row,col)
    #현재 위치 청소
    if board[row][col] == 0 :
        board[row][col] = 2
        move += 1
    #주변 전부 이미 청소함
    if isAllClean(row,col) : 
        # 후진
        nextRow,nextCol = move_backward(row,col,cur_dir)
        if nextRow == -1 and nextCol == -1 :
            break
        else :
            row = nextRow
            col = nextCol
    #주변에 청소할 곳이 있다
    else :
        #반시계로 90도 회전후 전진 가능 여부 확인
        nextRow , nextCol = rotate(row,col,0)
        row = nextRow
        col = nextCol
            
    

print(move)
