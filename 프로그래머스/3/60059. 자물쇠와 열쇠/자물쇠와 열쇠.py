def solution(key, lock):
    homes = 0
    for i in lock:
        for j in i :
            if j == 0 :
                homes += 1
    M = len(key)
    N = len(lock)
    def rotate(point_row,point_col,M):
        temp = []
        for i in range(len(point_row)):
            temp.append(point_row[i])
            point_row[i] = point_col[i]
            
        for i in range(len(point_col)):
            point_col[i] = M - 1 - temp[i]
        return point_row, point_col
    
    def check(startRow,startCol,point_row,point_col):
        count = 0
        # 각 키의 돌기에 대해 
        for i in range(len(point_row)):
            key_row = startRow + point_row[i]
            key_col = startCol + point_col[i]
            #범위 내에 있는것들에 대해 비교
            if 0 <= key_row < N and 0 <= key_col < N :
                # 키는 돌기인데 락은 구멍이면
                if lock[key_row][key_col] == 0:
                    count += 1
                    continue
                #키는 돌기인데 락도 구멍
                else :
                    return False
        if count == homes :
            return True
        
    answer = False
    point_row = []
    point_col = []
    
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                point_row.append(i)
                point_col.append(j)
    
    for startRow in range(-M + 1,N):
        for startCol in range(-M + 1,N):
            for i in range(4):
                point_row, point_col = rotate(point_row,point_col,M)
                if check(startRow,startCol,point_row,point_col):
                    return True
                
    return answer