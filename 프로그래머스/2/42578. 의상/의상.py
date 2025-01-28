def solution(clothes):
    hash = dict()
    
    for cloth in clothes :
        if cloth[1] not in hash :
            hash[cloth[1]] = 1
        else :
            hash[cloth[1]] += 1
    print(hash)
    answer = 1
    for i in hash :
        answer *= ( hash[i] + 1 )
    return answer - 1