from collections import deque
def solution(routes):
    answer = 0
    routes.sort(key = lambda x: [x[0],x[1]])
    routes = deque(routes)
    temp = routes.popleft()[1]
    answer += 1
    
    while routes :
        start, end = routes.popleft()
        if temp >= start :
            temp = min(end,temp)
        else :
            temp = end
            answer += 1
            
    return answer