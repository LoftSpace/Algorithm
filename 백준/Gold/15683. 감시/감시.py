import sys
import copy
input = sys.stdin.readline

N , M = map(int,input().split())
grid = []
for i in range(N):
    grid.append(list(map(int,input().split())))
cctv = 0
cctv_list = []
ans = 100000000

# 북 동 남 서
dRow =  [-1,0,1,0]
dCol = [0,1,0,-1]
mode = [
    [],
    [1],
    [1,3],
    [0,1],
    [0,1,3],
    [0,1,2,3]
]

for i in range(N):
    for j in range(M):
        if grid[i][j] != 0 and grid[i][j] != 6 :
            cctv += 1
            cctv_list.append([grid[i][j],i,j])
#print(cctv_list)

def search(rotate,cctv_num):
    cctv_row = cctv_list[cctv_num][1]
    cctv_col = cctv_list[cctv_num][2]
    cctv_type = cctv_list[cctv_num][0]
    direction = copy.deepcopy(mode[cctv_type])
    for i in range(len(direction)):
        direction[i] += rotate
        direction[i] %= 4

    #이동해야 하는 각 방향에 대해
    for dir in direction :
        nextRow = cctv_row
        nextCol = cctv_col
        while True :
            nextRow +=  dRow[dir]
            nextCol += dCol[dir]
            if 0 <= nextRow < N and 0 <= nextCol < M :
                if grid[nextRow][nextCol] == 6 :
                    break
                elif grid[nextRow][nextCol] <= 0 :
                    grid[nextRow][nextCol] -= 1
            else :
                break

def search_cancel(rotate,cctv_num):
    cctv_row = cctv_list[cctv_num][1]
    cctv_col = cctv_list[cctv_num][2]
    cctv_type = cctv_list[cctv_num][0]
    direction = copy.deepcopy(mode[cctv_type])
    for i in range(len(direction)):
        direction[i] += rotate
        direction[i] %= 4

    for dir in direction :
        nextRow = cctv_row
        nextCol = cctv_col
        while True :
            nextRow +=  dRow[dir]
            nextCol += dCol[dir]
            if 0 <= nextRow < N and 0 <= nextCol < M :
                if grid[nextRow][nextCol] == 6 :
                    break
                elif grid[nextRow][nextCol] <= 0 :
                    grid[nextRow][nextCol] += 1
            else :
                break

def find_area():
    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0 :
                count += 1
    return count

def dfs(cctv_num):
    global ans
    #print(cctv_num)
    if cctv_num == cctv :
     #   for i in grid :
      #      print(i)
       # print(find_area())
        ans = min(ans,find_area())
        return 
    for rotate in range(4):
        search(rotate,cctv_num)
        dfs(cctv_num + 1)
        
        search_cancel(rotate,cctv_num)

dfs(0)
print(ans)