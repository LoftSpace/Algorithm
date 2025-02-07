import math
def solution(n, stations, w):
    answer = 0
    start = 1
    m = len(stations)
    
    for station in stations:
        
        length = station - w - 1 - start + 1
        print(length,start)
        if length > 0 :
            if length <= 2 * w + 1 :
                answer += 1
            else :
                answer += math.ceil(length / ( 2 * w + 1) )
        
        start = station + w + 1
        if start > n :
            break
    
    #마지막 구역
    if start <= n:
        
        length = n - start  + 1
        print(length)
        if length > 0 :
            if length <= 2 * w + 1 :
                answer += 1
            else :
                answer += math.ceil(length / ( 2 * w + 1))
        


    return answer