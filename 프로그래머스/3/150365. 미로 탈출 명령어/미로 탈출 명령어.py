from collections import deque
import copy
def solution(n, m, x, y, r, c, k):
    def check_available2(cur_x,cur_y,move,k):
        for i in range(move + 1,k):
            if visited[cur_x][cur_y][i]:
                return False
        return True
    def check_available(cur_x,cur_y,move,k):
        move_remain = k - move
        distance = abs(r-cur_x) + abs(c - cur_y)
        if distance > move_remain :
            return False
        return True
    dX = [1,0,0,-1]
    dY = [0,-1,1,0]
    d = ['d','l','r','u']
    routes = []
    queue = deque([])
    p = []
    move = 0
    queue.append([x,y,p,move])
    visited = [[[False] * (k + 1) for i in range(m + 1) ] for j in range(n + 1)]
    
    while queue :
        cur_x,cur_y,path,move = queue.popleft()
      
        if move >= k :
            continue
        
        for dir in range(4):
            nextY = cur_y + dY[dir]
            nextX = cur_x + dX[dir]
            #print(nextY,nextX,n,m)
            if 0 < nextY <= m and 0 < nextX <= n :
                if not visited[nextX][nextY][move + 1] :
                    if  check_available(nextX,nextY,move + 1,k) :
                        if check_available2(nextX,nextY,move + 1,k):
                            if move + 1 == k :
                                if nextX == r and nextY == c :
                                    path.append(d[dir])
                                    return ''.join(path)
                            else :
                                visited[nextX][nextY][move + 1] = True
                                temp = copy.deepcopy(path)
                                temp.append(d[dir])
                                queue.append([nextX,nextY,temp,move + 1])
                            break
    
    if not routes :
        return "impossible"