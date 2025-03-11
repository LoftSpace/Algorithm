def solution(targets):
    targets.sort(key = lambda x : [x[0],x[1]])
    #print(targets)
    answer = 1
    
    end = targets[0][1]
    
    for target in targets :
        if target[0] >= end :
            answer += 1
            end = target[1]
        elif target[1] < end :
            end = target[1]
    
    return answer