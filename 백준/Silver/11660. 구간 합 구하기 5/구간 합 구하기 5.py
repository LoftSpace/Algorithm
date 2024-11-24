import sys

input = sys.stdin.readline

N, M = map(int,input().split())

grid =[]

arrSum = [[] for _ in range(N)]

for i in range(N) :
    grid.append(list(map(int,input().split())))

for i in range(N) :
    Sum = 0
    for j in range(N) :
        Sum += grid[i][j]

        arrSum[i].append(Sum)

for i in range(M) :
    row1, col1, row2, col2 = map(int,input().split())
    row1 -= 1
    col1 -= 1
    row2 -= 1
    col2 -= 1
    Sum = 0
    if col1 == 0 :
        for row in range(row1,row2 + 1) :
            Sum += arrSum[row][col2]
    else :
        for row in range(row1,row2 + 1) :
            #print("arrSum[%d][%d] - arrSum[%d][%d]"%(row,col2,row,col1-1))
            Sum += arrSum[row][col2] - arrSum[row][col1 - 1]
    
    print(Sum)