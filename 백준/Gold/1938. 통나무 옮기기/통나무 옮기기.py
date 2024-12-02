import sys
from collections import deque

input = sys.stdin.readline

dRow = [1,-1,0,0]
dCol = [0,0,1,-1]
N = int(input())
visited = [[[1000000] * 2 for _ in range(N)] for q in range(N)]

grid = []
bRow = 0
bCol = 0
bwORh = 0
eRow = 0
eCol = 0
ewORh = 0

for _ in range(N) :
    grid.append(list(input().strip()))

firstE = -1
secondE = -1
thirdE = -1
firstB = -1
secondB = -1
thirdB = -1
for i in range(N) :
    for j in range(N) :
        if grid[i][j] == 'E' :
            if firstE == -1 :
                firstE = i * N + j
            elif secondE == -1 :
                secondE = i * N + j
                
            else:
                thirdE = i * N + j
        if grid[i][j] == 'B' :
            if firstB == -1 :
                firstB = i * N + j
            elif secondB == -1 :
                secondB = i * N + j
                
            else:
                thirdB = i * N + j
        
if firstE == secondE - 1 :
    ewORh = 1
eRow = secondE // N
eCol = secondE % N
if firstB == secondB - 1 :
    bwORh = 1
bRow = secondB // N
bCol = secondB % N

            
def U(midRow,midCol, wORh) :
    if wORh == 1 :
        if midRow - 1 >= 0 :
            if grid[midRow-1][midCol-1] != '1' and grid[midRow-1][midCol] != '1' and grid[midRow-1][midCol+1] != '1' :
                return True
    else :
        if midRow - 2 >= 0 :
            if grid[midRow-2][midCol] != '1' :
                return True
    return False

def D(midRow,midCol, wORh):
    if wORh == 1 :
        if midRow + 1  < N :
            if grid[midRow+1][midCol-1] != '1' and grid[midRow+1][midCol] != '1' and grid[midRow+1][midCol+1] != '1' :
                return True
    else :
        if midRow + 2 < N :
            if grid[midRow+2][midCol] != '1' :
                return True
    return False
def L(midRow,midCol, wORh):
    if wORh == 1 :
        if midCol - 2 >= 0 :
            if grid[midRow][midCol-2] != '1' :
                return True
    else :
        if midCol - 1 >= 0:
            if grid[midRow-1][midCol-1] != '1' and grid[midRow][midCol-1] != '1' and grid[midRow+1][midCol-1] != '1' :
                return True
    return False

def R(midRow,midCol, wORh):
    if wORh == 1 :
        if midCol + 2 < N :
            if grid[midRow][midCol+2] != '1' :
                return True
    else :
        if midCol + 1 < N:
            if grid[midRow-1][midCol+1] != '1' and grid[midRow][midCol+1] != '1' and grid[midRow+1][midCol+1] != '1' :
                return True
    return False
def T(midRow,midCol, wORh):
    if not (0<= midRow -1 and 0<= midCol-1 and midRow +1 < N and midCol + 1 < N) :
        return False
    if wORh == 1 :
        if grid[midRow-1][midCol-1] != '1' and grid[midRow-1][midCol] != '1' and grid[midRow-1][midCol+1] != '1' and grid[midRow+1][midCol-1] != '1' and grid[midRow+1][midCol] != '1' and grid[midRow+1][midCol+1] != '1' :
            return True
    else :
        if grid[midRow-1][midCol-1] != '1' and grid[midRow][midCol-1] != '1' and grid[midRow+1][midCol-1] != '1' and grid[midRow-1][midCol+1] != '1' and grid[midRow][midCol+1] != '1' and grid[midRow+1][midCol+1] != '1' :
            return True
    return False


def BFS():
    queue = []
    queue = deque()
    queue.append([bRow,bCol,bwORh,0])

    while queue : 
        midRow, midCol, wORh , count = queue.popleft()
        #print( midRow, midCol, wORh , count)
        
        if midRow == eRow and midCol == eCol and wORh == ewORh :
            print(count)
            return
        
        if D(midRow,midCol,wORh) :
            if visited[midRow + 1][midCol][wORh] > count + 1 :
                queue.append([midRow + 1,midCol,wORh,count + 1])
                visited[midRow+1][midCol][wORh] = count + 1

        if U(midRow,midCol,wORh) :
            if visited[midRow - 1][midCol][wORh] > count + 1 :
                queue.append([midRow - 1,midCol,wORh,count + 1])
                visited[midRow - 1][midCol][wORh] = count + 1

        if L(midRow,midCol,wORh) :
            if visited[midRow][midCol - 1][wORh] > count + 1 :
                queue.append([midRow,midCol - 1,wORh,count + 1])
                visited[midRow][midCol - 1][wORh] = count + 1
        if R(midRow,midCol,wORh) :
            if visited[midRow][midCol + 1][wORh] > count + 1 :
                queue.append([midRow,midCol + 1,wORh,count + 1])
                visited[midRow][midCol + 1][wORh] = count + 1

        if T(midRow,midCol,wORh) :
            if wORh == 0 :
                wORh = 1
            else :
                wORh = 0

            if visited[midRow][midCol][wORh] > count + 1 :
                queue.append([midRow,midCol,wORh,count + 1])
                visited[midRow][midCol][wORh] = count + 1
    print(0)
        
BFS()