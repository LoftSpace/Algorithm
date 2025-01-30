from collections import deque

def solution(cacheSize, cities1):
    cities = []
    for i in cities1 :
        cities.append(i.lower())
    N = len(cities)
    queue = deque([])
    answer = 0
    hash = dict()
    if cacheSize == 0 :
        return N * 5
    for i in cities :
        hash[i] = False
        
    for city in cities :
        # 캐시에 있다면 
        if hash[city] == True :
            queue.remove(city)
            queue.append(city)
            answer += 1
        # 캐시에 없다면 
        else :
            #캐시에 자리가 있다면
            if not queue or len(queue) < cacheSize :
                queue.append(city)
                hash[city] = True
                answer += 5
            #캐시가 꽉 찼다면
            else :
                hash[queue.popleft()] = False
                hash[city] = True
                queue.append(city)
                answer += 5
       
    return answer