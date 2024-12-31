def distance(x1,y1,x2,y2):
    return (x1-x2) **2 + (y1-y2) ** 2
def solution(m, n, startX, startY, balls):
    answer = []
    for i in range(len(balls)):
        targetX = balls[i][0]
        targetY = balls[i][1]
        ans = 10000000
        #아래로 원쿠션
        if not(startX == targetX and startY >= targetY):
            ans = min(ans,distance(startX,-startY,targetX,targetY))
        #위로 원쿠션
        if not(startX == targetX and startY <= targetY):
            ans = min(ans,distance(startX,n + n - startY,targetX,targetY))
        #왼쪽으로
        if not(startY == targetY and startX >= targetX) :
            ans = min(ans,distance(-startX,startY,targetX,targetY))
        #오른쪽으로
        if not(startY == targetY and startX <= targetX):
            ans = min(ans,distance(m + m - startX,startY,targetX,targetY))
            
            
        answer.append(ans)
    
    return answer